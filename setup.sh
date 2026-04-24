#!/bin/bash
# =============================================================================
# CPS 141 — Environment Setup Script
# =============================================================================
# Run this once after cloning the repo:
#   chmod +x setup.sh
#   ./setup.sh
# =============================================================================

set -e  # exit immediately if anything fails

echo ""
echo "🐍 CPS 141 — Setting up your Python environment..."
echo "💛💙 Go Blue, Dylan!"
echo ""

# -----------------------------------------------------------------------------
# Check Python is available
# -----------------------------------------------------------------------------
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.11+ and try again."
    echo "   Download at: https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo "✅ Found $PYTHON_VERSION"

# -----------------------------------------------------------------------------
# Create virtual environment
# -----------------------------------------------------------------------------
if [ -d "venv" ]; then
    echo "⚠️  Virtual environment already exists — skipping creation."
else
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created."
fi

# -----------------------------------------------------------------------------
# Activate virtual environment
# -----------------------------------------------------------------------------
echo "⚡ Activating virtual environment..."
source venv/bin/activate

# -----------------------------------------------------------------------------
# Upgrade pip
# -----------------------------------------------------------------------------
echo "⬆️  Upgrading pip..."
pip install --upgrade pip --quiet

# -----------------------------------------------------------------------------
# Install dependencies
# -----------------------------------------------------------------------------
echo "📚 Installing dependencies from requirements.txt..."
pip install -r requirements.txt --quiet
echo "✅ All dependencies installed."

# -----------------------------------------------------------------------------
# Set up .env if it doesn't exist
# -----------------------------------------------------------------------------
if [ -f ".env" ]; then
    echo "⚠️  .env file already exists — skipping."
else
    echo "🔑 Creating .env from .env.sample..."
    cp .env.sample .env
    echo "✅ .env created. Open it and add your API keys before running notebooks."
fi

# -----------------------------------------------------------------------------
# Done
# -----------------------------------------------------------------------------
echo ""
echo "=============================================="
echo "✅ Setup complete!"
echo "=============================================="
echo ""
echo "Next steps:"
echo "  1. Open .env and add your API keys"
echo "  2. Activate your environment:  source venv/bin/activate"
echo "  3. Launch JupyterLab:          jupyter lab"
echo "  4. Or open in PyCharm and it will detect everything automatically."
echo ""
echo "💛💙 You're ready to code. Let's go!"
echo ""
