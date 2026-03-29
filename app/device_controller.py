from __future__ import annotations

import json
import subprocess
from pathlib import Path


def apply_control_signal(device_id: str, payload: dict) -> dict:
    state_path = Path("/tmp") / f"{device_id}.json"
    state_path.write_text(json.dumps(payload), encoding="utf-8")
    return {"device_id": device_id, "written": True}


def run_diagnostics(command: str) -> str:
    return subprocess.check_output(command, shell=True, text=True)  # noqa: S602,S603

