"""CS Career Compass — backend server.

This file does ONLY the things that genuinely need Python:
  1. Serve the static frontend files (HTML/CSS/JS) from ./public as-is.
  2. Expose a small JSON API that the frontend JavaScript calls:
       GET  /api/data   -> { fields: [...], items: {...} }   (all field + skill/tool data)
       POST /api/match  -> { skills, job, limit } -> match_jobs() result as JSON

No HTML, CSS or page markup is generated in Python anymore. All markup,
styling and page behavior live in normal web files under public/.
"""
from __future__ import annotations
import json
import mimetypes
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from career_data import FIELDS, ITEM_INFO
from career_model import match_jobs, learning_plan, model_info

APP_NAME = "CS Career Compass"
PORT = 8765
PUBLIC_DIR = (Path(__file__).parent / "public").resolve()


def field_by_id(fid: str):
    return next((f for f in FIELDS if f["id"] == fid), None)


class Handler(BaseHTTPRequestHandler):
    # ---------- helpers ----------
    def _send_json(self, payload, status: int = 200):
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_file(self, path: Path, status: int = 200):
        data = path.read_bytes()
        mime, _ = mimetypes.guess_type(str(path))
        self.send_response(status)
        self.send_header("Content-Type", (mime or "application/octet-stream") + (
            "; charset=utf-8" if (mime or "").startswith("text/") or (mime or "") in
            ("application/javascript", "application/json") else ""
        ))
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _safe_static_path(self, url_path: str) -> "Path | None":
        """Resolve a URL path to a file inside PUBLIC_DIR, blocking path traversal."""
        rel = url_path.lstrip("/") or "index.html"
        candidate = (PUBLIC_DIR / rel).resolve()
        if PUBLIC_DIR not in candidate.parents and candidate != PUBLIC_DIR:
            return None
        if candidate.is_dir():
            candidate = candidate / "index.html"
        return candidate

    # ---------- routing ----------
    def do_GET(self):
        u = urlparse(self.path)

        if u.path == "/api/data":
            self._send_json({"fields": FIELDS, "items": ITEM_INFO, "model": model_info()})
            return

        if u.path.startswith("/api/field/"):
            parts = u.path.split("/")
            fid = parts[3] if len(parts) > 3 else ""
            f = field_by_id(fid)
            if f:
                self._send_json(f)
            else:
                self._send_json({"error": "field not found"}, status=404)
            return

        # everything else -> static file from public/
        path = self._safe_static_path(u.path)
        if path is None or not path.exists() or not path.is_file():
            not_found = PUBLIC_DIR / "404.html"
            if not_found.exists():
                self._send_file(not_found, status=404)
            else:
                self._send_json({"error": "not found"}, status=404)
            return
        self._send_file(path)

    def do_POST(self):
        u = urlparse(self.path)
        if u.path != "/api/match":
            self._send_json({"error": "not found"}, status=404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length).decode("utf-8", "replace") if length else "{}"
        try:
            body = json.loads(raw) if raw.strip() else {}
        except json.JSONDecodeError:
            self._send_json({"error": "invalid JSON body"}, status=400)
            return

        skills = str(body.get("skills", "")).strip()
        job = str(body.get("job", "")).strip()
        limit = int(body.get("limit", 10) or 10)

        if len(skills) < 2:
            self._send_json({"error": "Enter at least one skill."}, status=400)
            return

        result = match_jobs(skills, job, limit)
        result["learning_plan"] = learning_plan(result["results"])
        self._send_json(result)

    def log_message(self, *args):
        pass


def run(open_browser: bool = True):
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    if open_browser:
        webbrowser.open(f"http://127.0.0.1:{PORT}/")
    print(f"{APP_NAME} running at http://127.0.0.1:{PORT}/")
    server.serve_forever()


if __name__ == "__main__":
    run()
