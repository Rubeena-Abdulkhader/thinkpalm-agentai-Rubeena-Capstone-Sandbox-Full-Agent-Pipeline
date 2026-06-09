#!/usr/bin/env python3
"""Launch SDLC Pipeline Studio."""

import socket
import sys
from pathlib import Path

import uvicorn

sys.path.insert(0, str(Path(__file__).resolve().parent))


def _port_free(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) != 0


def _pick_port(preferred: int = 3000) -> int:
    if _port_free(preferred):
        return preferred
    for alt in (3001, 3002, 8080):
        if _port_free(alt):
            print(f"Port {preferred} is in use (likely old ArchReview server).")
            print(f"Using port {alt} instead.")
            return alt
    return preferred


def main() -> None:
    port = _pick_port(3000)
    print(f"SDLC Agent Pipeline Studio -> http://localhost:{port}")
    print("Press Ctrl+C to stop.")
    if port != 3000:
        print("TIP: Stop the old server on port 3000 (Ctrl+C in that terminal) to use the default port.")
    uvicorn.run("src.ui.studio.server:app", host="0.0.0.0", port=port, reload=False)


if __name__ == "__main__":
    main()
