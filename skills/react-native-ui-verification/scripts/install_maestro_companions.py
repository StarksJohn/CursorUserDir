#!/usr/bin/env python3

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Any, Dict, List


COMPANION_APKS = ("maestro-app.apk", "maestro-server.apk")


def run(command: List[str]) -> Dict[str, Any]:
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )
    output = (result.stdout or result.stderr).strip()
    return {
        "ok": result.returncode == 0,
        "exitCode": result.returncode,
        "output": output[-2000:],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Preinstall official Maestro companion APKs through adb. "
            "This repairs vendor-specific streamed-install failures and is not E2E evidence."
        )
    )
    parser.add_argument("--device", required=True, help="Android adb serial")
    parser.add_argument(
        "--maestro-jar",
        type=Path,
        default=Path.home() / ".maestro" / "lib" / "maestro-client.jar",
    )
    args = parser.parse_args()

    adb = shutil.which("adb")
    if not adb:
        print("adb is not available in PATH", file=sys.stderr)
        return 2

    maestro_jar = args.maestro_jar.expanduser().resolve()
    if not maestro_jar.is_file():
        print(f"Maestro client JAR does not exist: {maestro_jar}", file=sys.stderr)
        return 2

    device_check = run([adb, "-s", args.device, "get-state"])
    if not device_check["ok"] or device_check["output"] != "device":
        print(
            f"Android device is not ready: {device_check['output']}",
            file=sys.stderr,
        )
        return 2

    results: Dict[str, Dict[str, Any]] = {}
    with tempfile.TemporaryDirectory(prefix="maestro-companions-") as temp_dir:
        temp_path = Path(temp_dir)
        try:
            with zipfile.ZipFile(maestro_jar) as archive:
                for apk_name in COMPANION_APKS:
                    archive.extract(apk_name, temp_path)
        except (OSError, KeyError, zipfile.BadZipFile) as error:
            print(f"Cannot extract Maestro companion APKs: {error}", file=sys.stderr)
            return 2

        for apk_name in COMPANION_APKS:
            result = run(
                [
                    adb,
                    "-s",
                    args.device,
                    "install",
                    "-r",
                    "-t",
                    str(temp_path / apk_name),
                ]
            )
            results[apk_name] = result
            if not result["ok"]:
                print(
                    json.dumps(
                        {
                            "device": args.device,
                            "companionInstallVerified": False,
                            "stableE2E": False,
                            "results": results,
                        },
                        ensure_ascii=False,
                        indent=2,
                    ),
                    file=sys.stderr,
                )
                return 1

    print(
        json.dumps(
            {
                "device": args.device,
                "companionInstallVerified": True,
                "stableE2E": False,
                "results": results,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
