#!/bin/bash

# --- Script Setup ---
# This script runs a 'lue-reader' container to read a book file.

# --- Path Processing ---
# Use the value of the environment variable if it exists, otherwise use the default.
# The ${VARIABLE:-default_value} syntax provides a default if VARIABLE is unset or empty.
BOOK_FULL_PATH="${BOOK_FULL_PATH:-sample.txt}"
MODELS_DIR="${MODELS_DIR:-/tmp}"
LOG_DIR="${LOG_DIR:-/tmp}"
TTS_MODEL="${TTS_MODEL:-edge}"

# Extract the directory from the full book path for the volume mount.
# Example: /home/user/books/war-of-art.txt -> /home/user/books
BOOK_DIR=$(dirname "$BOOK_FULL_PATH")

# Extract the filename from the full book path to be used inside the container.
# Example: /home/user/books/war-of-art.txt -> war-of-art.txt
BOOK_FILENAME=$(basename "$BOOK_FULL_PATH")

# --- Usage Information ---
echo "Starting lue-reader with the following settings:"
echo "  BOOK_FULL_PATH: $BOOK_FULL_PATH"
echo "  MODELS_DIR: $MODELS_DIR"
echo "  LOG_DIR: $LOG_DIR"
echo "  TTS_MODEL: $TTS_MODEL"
echo "---"


# --- Podman Command ---
# Run the container
# -it: Run in interactive mode with a TTY, so you can use the reader.
# --rm: Automatically remove the container when you exit.
# --replace: Replace the container if it already exists.
# --name: Give the container a name.
# -v: Mount a local directory to a directory inside the container.
#  - mounts directory where the book is saved.
#  - a directory the containerized application will stream logs to.
#  - a directory on the host to download models from hugging face into.
#    (it is a bad practice to store model weights on container volumes)
# -e: Set environment variables.
#   - PULSE_SERVER: allows the container to access the host sound device.
#   - XDG_DATA_HOME: specify the log directory in the container (which is bind mounted).
# --device: Give the container access to GPU devices.
# --security-opt: Set security options.

podman run -it --rm --replace --name lue-app \
  -e PULSE_SERVER=unix:/run/user/$(id -u)/pulse/native \
  -v /run/user/$(id -u)/pulse/native:/run/user/$(id -u)/pulse/native \
  -v "$BOOK_DIR:/app/books:z" \
  -v "$LOG_DIR:/root/.local/state/lue/log:z" \
  -v "$MODELS_DIR:/root/.local/share:z" \
  -e XDG_DATA_HOME="/root/.local/share" \
  --device nvidia.com/gpu=all \
  --security-opt=label=disable \
  lue-reader --tts $TTS_MODEL \
  "/app/books/$BOOK_FILENAME"
