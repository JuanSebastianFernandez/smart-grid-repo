from __future__ import annotations

def apply_control_signal(device_id: str, payload: dict) -> dict:
    return {"device_id": device_id, "accepted": True, "payload": payload}


def run_diagnostics(command: str) -> str:
    return f"diagnostics-blocked:{command}"
