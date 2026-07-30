## Linux Prerequisites (System-Level)

Before running `pip install -r requirements-linux.txt`, install system dependencies:

### Ubuntu/Debian

bash sudo apt update && sudo apt install portaudio19-dev build-essential

### Arch/Manjaro

bash sudo pacman -S portaudio base-devel

### Fedora

bash sudo dnf install portaudio-devel gcc gcc-c++ make

### openSUSE

bash sudo zypper install portaudio-devel gcc make

### After System Install

bash source .venv/bin/activate CMAKE_ARGS="-DLLAMA_CUDA=on" pip install --upgrade -r requirements-linux.txt pip install --upgrade -r requirements-local.txt