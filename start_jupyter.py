from __future__ import annotations

import secrets
import socket
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8888
MAX_PORT_ATTEMPTS = 25


def find_available_port(host: str, start_port: int, attempts: int) -> int:
    for port in range(start_port, start_port + attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind((host, port))
            except OSError:
                continue
            return port

    raise RuntimeError(f"Could not find an available port between {start_port} and {start_port + attempts - 1}.")


def main() -> None:
    port = find_available_port(DEFAULT_HOST, DEFAULT_PORT, MAX_PORT_ATTEMPTS)
    token = secrets.token_urlsafe(24)
    url = f"http://{DEFAULT_HOST}:{port}/lab?token={token}"

    print("")
    print("JupyterLab is starting...")
    print(f"Project root: {ROOT}")
    print(f"Open this URL in a browser: {url}")
    print("")

    command = [
        sys.executable,
        "-m",
        "jupyterlab",
        f"--ServerApp.ip={DEFAULT_HOST}",
        f"--ServerApp.port={port}",
        "--ServerApp.port_retries=0",
        f"--ServerApp.token={token}",
        "--ServerApp.open_browser=False",
        f"--ServerApp.root_dir={ROOT}",
    ]
    subprocess.run(command, check=True, cwd=ROOT)


if __name__ == "__main__":
    main()
