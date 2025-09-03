# Use an older, stable Python base image based on Debian Bullseye
FROM python:3.10-slim-bookworm

# Set non-interactive frontend for package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies required by lue
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    espeak \
    antiword \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# 1. Copy only the dependency definition files first
COPY requirements.txt pyproject.toml ./

# 2. Install Python dependencies (this layer is now cached)
RUN pip install --no-cache-dir -r requirements.txt

# 3. (Optional) Install pytorch dependencies required by the kokoro TTS model, or any other offline model other than the edge TTS.
# CUDA option:
# RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# CPU option:
# RUN pip install torch torchvision torchaudio

# 4. Now, copy the rest of the application code
COPY . .

# 5. Install the lue application itself (this will be quick)
RUN pip install .

# Set the entry point
ENTRYPOINT ["lue"]
