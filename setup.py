from __future__ import annotations

import platform
import shutil
import subprocess
import sys
import venv
from pathlib import Path


ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / "venv"
REQUIREMENTS_FILE = ROOT / "requirements.txt"
ENV_FILE = ROOT / ".env"
ENV_SAMPLE_FILE = ROOT / ".env.sample"
MIN_PYTHON = (3, 11)


def echo(message: str = "") -> None:
    print(message)


def fail(message: str, exit_code: int = 1) -> None:
    echo(message)
    raise SystemExit(exit_code)


def detect_os() -> str:
    system = platform.system()
    if system == "Darwin":
        return "macOS"
    if system == "Windows":
        return "Windows"
    if system == "Linux":
        return "Linux"
    return system or "Unknown"


def ensure_python_version() -> None:
    version = sys.version_info[:3]
    if version < MIN_PYTHON:
        fail(
            f"❌ Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+ is required. "
            f"You are using {version[0]}.{version[1]}.{version[2]}."
        )


def create_virtualenv() -> None:
    if VENV_DIR.exists():
        echo("⚠️  Virtual environment already exists — skipping creation.")
        return

    echo("📦 Creating virtual environment...")
    venv.EnvBuilder(with_pip=True).create(VENV_DIR)
    echo("✅ Virtual environment created.")


def get_venv_python() -> Path:
    candidates = [
        VENV_DIR / "Scripts" / "python.exe",
        VENV_DIR / "bin" / "python",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate

    fail(
        "❌ Could not find the virtual environment's Python executable.\n"
        "   Expected one of:\n"
        "   - venv/Scripts/python.exe\n"
        "   - venv/bin/python"
    )
    raise AssertionError("unreachable")


def run_command(command: list[str]) -> None:
    subprocess.run(command, check=True, cwd=ROOT)


def install_dependencies(venv_python: Path) -> None:
    echo("⬆️  Upgrading pip...")
    run_command([str(venv_python), "-m", "pip", "install", "--upgrade", "pip", "--quiet"])

    echo("📚 Installing dependencies from requirements.txt...")
    run_command([str(venv_python), "-m", "pip", "install", "-r", str(REQUIREMENTS_FILE), "--quiet"])
    echo("✅ All dependencies installed.")


def ensure_env_file() -> None:
    if ENV_FILE.exists():
        echo("⚠️  .env file already exists — skipping.")
        return

    if ENV_SAMPLE_FILE.exists():
        echo("🔑 Creating .env from .env.sample...")
        shutil.copyfile(ENV_SAMPLE_FILE, ENV_FILE)
        echo("✅ .env created. Open it and add your API keys before running notebooks.")
        return

    echo("⚠️  .env.sample not found — skipping .env creation.")


def print_next_steps(os_name: str) -> None:
    echo("")
    echo("==============================================")
    echo("✅ Setup complete!")
    echo("==============================================")
    echo("")
    echo("Next steps:")
    echo("  1. Open .env and add your API keys (if needed)")
    if os_name == "Windows":
        echo(r"  2. Activate your environment (PowerShell):  .\venv\Scripts\Activate.ps1")
        echo(r"     Or Command Prompt:                       venv\Scripts\activate.bat")
        echo(r"     Or Git Bash:                             source venv/Scripts/activate")
    else:
        echo("  2. Activate your environment:              source venv/bin/activate")
    echo("  3. Launch JupyterLab:                       jupyter lab")
    echo("  4. Or open in PyCharm and select the interpreter inside venv.")
    echo("")
    echo("💛💙 You're ready to code. Let's go!")
    echo("")


def main() -> None:
    echo("")
    echo("🐍 CPS 141 — Setting up your Python environment...")
    echo("💛💙 Go Blue, Dylan!")
    echo("")

    ensure_python_version()

    os_name = detect_os()
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    echo(f"✅ Found Python {python_version}")
    echo(f"💻 Detected OS: {os_name}")

    create_virtualenv()
    venv_python = get_venv_python()
    echo(f"✅ Using virtual environment at {VENV_DIR.name}")

    install_dependencies(venv_python)
    ensure_env_file()
    print_next_steps(os_name)


if __name__ == "__main__":
    main()
