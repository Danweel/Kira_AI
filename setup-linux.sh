#!/bin/bash
set -e

echo "=== Kira Linux Setup ==="

# Check venv
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Activating venv..."
    source .venv/bin/activate  # Assuming you run this FROM ~/Kira/Kira/
fi

# Install main requirements
echo "[1/3] Installing requirements..."
pip install --upgrade -r requirements-linux.txt

# Install llama-cpp-python with CUDA
echo "[2/3] Installing llama-cpp-python with CUDA support..."
CMAKE_ARGS="-DLLAMA_CUDA=on" pip install --upgrade -r requirements-local.txt

# Verify
echo "[3/3] Verifying installation..."
pip list | grep -E "llama|pyaudio|fastapi|webrtcvad|uvicorn"

echo ""
echo "=== Setup complete! Run: python run.py ==="