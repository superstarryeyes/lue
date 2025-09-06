#!/bin/bash

# --- Script Setup ---
# A robust, cross-platform script to run the 'lue-reader' container.

# --- User-Configurable Ports ---
# Users can override these defaults by setting the environment variables before running the script.
# Example: MACOS_PORT=12346 ./run.sh
MACOS_PORT="${MACOS_PORT:-12345}"
WINDOWS_PORT="${WINDOWS_PORT:-4713}"

# --- Path Processing ---
BOOK_FULL_PATH="${BOOK_FULL_PATH:-sample.txt}"
MODELS_DIR="${MODELS_DIR:-/tmp}"
LOG_DIR="${LOG_DIR:-.}"
TTS_MODEL="${TTS_MODEL:-edge}"

BOOK_DIR=$(dirname "$BOOK_FULL_PATH")
BOOK_FILENAME=$(basename "$BOOK_FULL_PATH")

# --- OS-Specific Audio Configuration ---
AUDIO_ARGS=""
OS="$(uname -s)"
SOCAT_PID=""

# Function to clean up background processes on exit
cleanup() {
    if [ -n "$SOCAT_PID" ]; then
        echo "Stopping background audio bridge..."
        kill "$SOCAT_PID"
    fi
}
trap cleanup EXIT

case "${OS}" in
    Linux*)
        echo "Configuring for Linux with PulseAudio..."
        # This is the standard, most reliable method for Linux desktops.
        AUDIO_ARGS="-e PULSE_SERVER=unix:/run/user/$(id -u)/pulse/native -v /run/user/$(id -u)/pulse/native:/run/user/$(id -u)/pulse/native"
        ;;
    Darwin*)
        echo "Configuring for macOS..."
        if ! command -v socat &> /dev/null; then
            echo "Error: 'socat' is not installed. Please run 'brew install socat' first."
            exit 1
        fi

        echo "Starting background audio bridge on port ${MACOS_PORT}..."
        # Create a temporary directory for the socket if it doesn't exist
        mkdir -p /tmp/pulse
        socat TCP-LISTEN:${MACOS_PORT},reuseaddr,fork UNIX-CONNECT:/tmp/pulse/native &
        SOCAT_PID=$!

        # --- Robust Readiness Check ---
        # Ping the server with retries instead of using a fixed sleep.
        echo "Waiting for audio bridge to be ready..."
        for i in {1..10}; do
            if nc -z 127.0.0.1 ${MACOS_PORT}; then
                echo "Audio bridge is active."
                break
            fi
            sleep 0.2
        done
        if ! nc -z 127.0.0.1 ${MACOS_PORT}; then
            echo "Error: Audio bridge failed to start in time."
            exit 1
        fi

        HOST_IP="host.docker.internal" # Use Docker's internal DNS for the host
        AUDIO_ARGS="-e PULSE_SERVER=tcp:${HOST_IP}:${MACOS_PORT}"
        ;;
    CYGWIN*|MINGW*|MSYS*)
        echo "Configuring for Windows..."
        HOST_IP="host.docker.internal"
        AUDIO_ARGS="-e PULSE_SERVER=tcp:${HOST_IP}:${WINDOWS_PORT}"
        echo "Attempting to connect to PulseAudio server at ${HOST_IP}:${WINDOWS_PORT}"
        ;;
    *)
        echo "Unsupported OS: ${OS}. Audio might not work."
        ;;
esac

# --- Usage Information ---
echo "Starting lue-reader..."
echo "---"

# --- Docker Command ---
docker run -it --rm --name lue-app \
  ${AUDIO_ARGS} \
  -v "$BOOK_DIR:/app/books" \
  -v "$LOG_DIR:/root/.local/state/lue" \
  -v "$MODELS_DIR:/root/.local/share" \
  -e XDG_DATA_HOME="/root/.local/share" \
  --gpus all \
  lue-reader --tts "$TTS_MODEL" \
  "/app/books/$BOOK_FILENAME"
