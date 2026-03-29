from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse


class SmartGridHandler(BaseHTTPRequestHandler):
    server_version = "VestaSmartGrid/0.1"

    def _write_json(self, payload: dict, status: int = 200) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args) -> None:
        return

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path == "/health":
            self._write_json({"status": "ok", "service": "smartgrid-app"})
            return
        if parsed.path == "/grid/status":
            self._write_json({"substations": 4, "load": 0.71, "alerts": 1, "mode": "runtime-attackable"})
            return
        if parsed.path == "/api/admin/run":
            cmd = parse_qs(parsed.query).get("cmd", [""])[0]
            self._write_json(
                {
                    "status": "blocked",
                    "message": "Admin command endpoint should not be exposed in production.",
                    "cmd": cmd,
                },
                status=500,
            )
            return
        self._write_json({"error": "not_found"}, status=404)

    def do_POST(self) -> None:  # noqa: N802
        self._write_json({"accepted": True}, status=202)


def main() -> None:
    server = ThreadingHTTPServer(("0.0.0.0", 8000), SmartGridHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()

