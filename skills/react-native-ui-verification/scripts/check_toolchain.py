#!/usr/bin/env python3

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


def run_command(command: List[str], cwd: Path) -> Dict[str, Any]:
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        return {"ok": False, "output": str(error)}

    output = (result.stdout or result.stderr).strip()
    return {
        "ok": result.returncode == 0,
        "exitCode": result.returncode,
        "output": output[:2000],
    }


def load_package_json(project_root: Path) -> Dict[str, Any]:
    package_path = project_root / "package.json"
    if not package_path.is_file():
        return {}

    try:
        return json.loads(package_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot read {package_path}: {error}") from error


def load_local_policy() -> Dict[str, Any]:
    policy_path = Path(__file__).resolve().parents[1] / "local-policy.json"
    if not policy_path.is_file():
        return {}

    try:
        return json.loads(policy_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot read {policy_path}: {error}") from error


def dependencies(package: Dict[str, Any]) -> Dict[str, str]:
    merged: Dict[str, str] = {}
    for key in ("dependencies", "devDependencies", "peerDependencies"):
        values = package.get(key, {})
        if isinstance(values, dict):
            merged.update(
                {str(name): str(version) for name, version in values.items()}
            )
    return merged


def scripts_contain(package: Dict[str, Any], terms: Iterable[str]) -> bool:
    scripts = package.get("scripts", {})
    if not isinstance(scripts, dict):
        return False

    combined = "\n".join(str(command).lower() for command in scripts.values())
    return any(term.lower() in combined for term in terms)


def count_matches(project_root: Path, patterns: Iterable[str]) -> int:
    matches = set()
    for pattern in patterns:
        for path in project_root.glob(pattern):
            if path.is_file() and "node_modules" not in path.parts:
                matches.add(path)
    return len(matches)


def resolve_tool(name: str) -> Optional[str]:
    path = shutil.which(name)
    if path:
        return path

    fallback_paths = {
        "maestro": Path.home() / ".maestro" / "bin" / "maestro",
    }
    fallback = fallback_paths.get(name)
    if fallback and fallback.is_file():
        return str(fallback)
    return None


def tool_info(name: str, version_command: Optional[List[str]], cwd: Path) -> Dict[str, Any]:
    path = resolve_tool(name)
    info: Dict[str, Any] = {"available": path is not None, "path": path}
    if path and version_command:
        resolved_command = [path, *version_command[1:]]
        version = run_command(resolved_command, cwd)
        info["versionCheck"] = version
    return info


def npm_global_versions(cwd: Path) -> Dict[str, str]:
    result = run_command(["npm", "list", "--global", "--depth=0", "--json"], cwd)
    if not result.get("ok"):
        return {}

    try:
        payload = json.loads(result.get("output", "{}"))
    except json.JSONDecodeError:
        return {}

    values = payload.get("dependencies", {})
    if not isinstance(values, dict):
        return {}

    return {
        str(name): str(metadata.get("version", "unknown"))
        for name, metadata in values.items()
        if isinstance(metadata, dict)
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Report global mobile automation availability and per-project "
            "React Native E2E integration."
        )
    )
    parser.add_argument("project_root", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args()

    project_root = args.project_root.expanduser().resolve()
    if not project_root.is_dir():
        print(f"project directory does not exist: {project_root}", file=sys.stderr)
        return 2

    try:
        package = load_package_json(project_root)
        local_policy = load_local_policy()
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 2

    deps = dependencies(package)
    global_versions = npm_global_versions(project_root)

    maestro_flows = count_matches(
        project_root,
        (".maestro/**/*.yaml", ".maestro/**/*.yml"),
    )
    detox_configs = count_matches(
        project_root,
        (
            ".detoxrc",
            ".detoxrc.*",
            "detox.config.*",
            "e2e/jest.config.*",
        ),
    )
    detox_tests = count_matches(
        project_root,
        ("e2e/**/*.test.*", "e2e/**/*.spec.*"),
    )
    appium_assets = count_matches(
        project_root,
        (
            "wdio.conf.*",
            "appium.config.*",
            "appium/**/*.js",
            "appium/**/*.ts",
            "e2e/**/*appium*",
        ),
    )

    appium_driver_check = (
        run_command(
            [resolve_tool("appium") or "appium", "driver", "list", "--installed"],
            project_root,
        )
        if resolve_tool("appium")
        else {"ok": False, "output": "appium is not available"}
    )

    detox_local_dependency = "detox" in deps
    detox_project_config = detox_configs > 0 or isinstance(package.get("detox"), dict)
    appium_client_dependency = any(
        name in deps
        for name in (
            "appium",
            "webdriverio",
            "wdio",
            "@wdio/cli",
            "appium-webdriveragent",
        )
    )

    report = {
        "projectRoot": str(project_root),
        "reactNativeProject": "react-native" in deps,
        "localPolicy": local_policy,
        "levels": {
            "globalAvailable": (
                "the CLI can start; this is not project E2E evidence"
            ),
            "projectConfigured": (
                "the repository has tool-specific dependencies/config/flows; "
                "this is not proof that a test passes"
            ),
            "currentRunVerified": (
                "false here by design; only an actual passing run against the "
                "current build and target state creates E2E evidence"
            ),
        },
        "tools": {
            "adb": tool_info("adb", ["adb", "version"], project_root),
            "xcrun": tool_info("xcrun", None, project_root),
            "maestro": {
                **tool_info("maestro", ["maestro", "--version"], project_root),
                "projectConfigured": maestro_flows > 0,
                "flowCount": maestro_flows,
                "currentRunVerified": False,
            },
            "appium": {
                **tool_info("appium", ["appium", "--version"], project_root),
                "globalPackageVersion": global_versions.get("appium"),
                "driverCheck": appium_driver_check,
                "projectConfigured": appium_client_dependency and appium_assets > 0,
                "clientDependency": appium_client_dependency,
                "configOrTestFileCount": appium_assets,
                "currentRunVerified": False,
            },
            "detox": {
                **tool_info("detox", None, project_root),
                "globalCliVersion": global_versions.get("detox-cli"),
                "projectConfigured": (
                    detox_local_dependency
                    and detox_project_config
                    and detox_tests > 0
                ),
                "localDependency": detox_local_dependency,
                "configPresent": detox_project_config,
                "testFileCount": detox_tests,
                "currentRunVerified": False,
                "note": (
                    "The global detox-cli only forwards to a repository-local "
                    "Detox executable."
                ),
            },
        },
    }

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
