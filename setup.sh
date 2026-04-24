#!/bin/bash
# Thin wrapper for users who still prefer ./setup.sh.

set -e

if command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_CMD="python"
else
    echo "❌ Python 3.11+ not found. Install Python and rerun setup."
    exit 1
fi

exec "$PYTHON_CMD" setup.py
