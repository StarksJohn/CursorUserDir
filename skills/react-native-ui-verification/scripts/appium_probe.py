#!/usr/bin/env python3

import argparse
import base64
import json
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, Optional


def request_json(
    base_url: str,
    method: str,
    path: str,
    payload: Optional[Dict[str, Any]] = None,
    timeout: int = 120,
) -> Dict[str, Any]:
    data = json.dumps(payload).encode() if payload is not None else None
    request = urllib.request.Request(
        base_url + path,
        data=data,
        method=method,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode())


def available_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("127.0.0.1", 0))
        return int(server.getsockname()[1])


def wait_for_server(base_url: str, process: subprocess.Popen[Any]) -> None:
    deadline = time.monotonic() + 30
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError(f"Appium exited with code {process.returncode}")
        try:
            response = request_json(base_url, "GET", "/status", timeout=2)
            if response.get("value", {}).get("ready") is True:
                return
        except (OSError, urllib.error.URLError, json.JSONDecodeError):
            time.sleep(0.5)
    raise RuntimeError("Appium did not become ready within 30 seconds")


def build_capabilities(args: argparse.Namespace) -> Dict[str, Any]:
    platform_name = "Android" if args.platform == "android" else "iOS"
    automation_name = "UiAutomator2" if args.platform == "android" else "XCUITest"
    capabilities: Dict[str, Any] = {
        "platformName": platform_name,
        "appium:automationName": automation_name,
        "appium:udid": args.device,
        "appium:deviceName": args.device,
        "appium:noReset": True,
        "appium:newCommandTimeout": 60,
        "appium:shouldTerminateApp": False,
    }

    if args.platform == "android":
        capabilities.update(
            {
                "appium:appPackage": args.app_id,
                "appium:appActivity": args.activity,
                "appium:dontStopAppOnReset": True,
            }
        )
    else:
        capabilities["appium:bundleId"] = args.app_id

    return capabilities


def parser() -> argparse.ArgumentParser:
    argument_parser = argparse.ArgumentParser(
        description=(
            "Create a no-reset Appium session and collect structural evidence. "
            "This probe is not a stable E2E test."
        )
    )
    argument_parser.add_argument("--platform", choices=("android", "ios"), required=True)
    argument_parser.add_argument("--device", required=True)
    argument_parser.add_argument("--app-id", required=True)
    argument_parser.add_argument(
        "--activity",
        help="Required Android launch activity, including its package or leading dot",
    )
    argument_parser.add_argument(
        "--screenshot",
        type=Path,
        help="Optional output path; screenshots may contain sensitive user data",
    )
    return argument_parser


def main() -> int:
    args = parser().parse_args()
    if args.platform == "android" and not args.activity:
        print("--activity is required for Android", file=sys.stderr)
        return 2

    appium = shutil.which("appium")
    if not appium:
        print("appium is not available in PATH", file=sys.stderr)
        return 2

    port = available_port()
    base_url = f"http://127.0.0.1:{port}"
    session_id: Optional[str] = None

    with tempfile.TemporaryFile(mode="w+t", encoding="utf-8") as server_log:
        process = subprocess.Popen(
            [appium, "--address", "127.0.0.1", "--port", str(port)],
            stdout=server_log,
            stderr=subprocess.STDOUT,
            text=True,
        )
        try:
            wait_for_server(base_url, process)
            response = request_json(
                base_url,
                "POST",
                "/session",
                {"capabilities": {"alwaysMatch": build_capabilities(args)}},
            )
            value = response.get("value", {})
            session_id = value.get("sessionId") or response.get("sessionId")
            if not session_id:
                raise RuntimeError("Appium did not return a session ID")

            source = request_json(
                base_url,
                "GET",
                f"/session/{session_id}/source",
            ).get("value", "")

            screenshot_path = None
            if args.screenshot:
                encoded = request_json(
                    base_url,
                    "GET",
                    f"/session/{session_id}/screenshot",
                ).get("value")
                if not isinstance(encoded, str):
                    raise RuntimeError("Appium did not return a screenshot")
                args.screenshot.parent.mkdir(parents=True, exist_ok=True)
                args.screenshot.write_bytes(base64.b64decode(encoded))
                screenshot_path = str(args.screenshot)

            print(
                json.dumps(
                    {
                        "probeOnly": True,
                        "stableE2E": False,
                        "platform": args.platform,
                        "device": args.device,
                        "appId": args.app_id,
                        "sessionCreated": True,
                        "sourceCharacters": len(source),
                        "screenshot": screenshot_path,
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
            return 0
        except (
            OSError,
            RuntimeError,
            urllib.error.URLError,
            json.JSONDecodeError,
        ) as error:
            server_log.seek(0)
            log_tail = server_log.read()[-3000:]
            print(str(error), file=sys.stderr)
            if log_tail:
                print(log_tail, file=sys.stderr)
            return 1
        finally:
            if session_id:
                try:
                    request_json(
                        base_url,
                        "DELETE",
                        f"/session/{session_id}",
                        timeout=30,
                    )
                except (OSError, urllib.error.URLError, json.JSONDecodeError):
                    pass
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)


if __name__ == "__main__":
    raise SystemExit(main())
