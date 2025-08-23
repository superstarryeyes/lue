"""Configuration settings for the Lue eBook reader."""

import os
from platformdirs import user_data_dir, user_cache_dir

# Default TTS model
DEFAULT_TTS_MODEL = "edge"

# Default voices for TTS models
TTS_VOICES = {
    "edge": "en-US-JennyNeural",
    "kokoro": "af_heart",
    "elevenlabs": "Peter Harwood",  # Default ElevenLabs voice
}

# Language codes for TTS models that require them
TTS_LANGUAGE_CODES = {
    "kokoro": "a",  # a=English, e=Spanish, j=Japanese, etc.
}

# TTS model-specific seconds of overlap between sentences (overrides default OVERLAP_SECONDS if specified)
TTS_OVERLAP_SECONDS = {
    "kokoro": 0.6,
}

# Audio processing settings
AUDIO_DATA_DIR = user_cache_dir("lue")
os.makedirs(AUDIO_DATA_DIR, exist_ok=True)
AUDIO_BUFFERS = [os.path.join(AUDIO_DATA_DIR, f"buffer_{i}") for i in range(6)]
MAX_QUEUE_SIZE = 4
OVERLAP_SECONDS = 0.5 # Seconds of overlap between sentences

# Progress tracking settings
PROGRESS_FILE_DIR = user_data_dir("lue")
os.makedirs(PROGRESS_FILE_DIR, exist_ok=True)

# General settings
SHOW_ERRORS_ON_EXIT = True

# PDF parsing settings
PDF_FILTERS_ENABLED = False  # You can also enable this with the --filter or -f command-line option
PDF_FILTER_HEADERS_BY_POSITION = True  # Filter headers in top margin of pages
PDF_FILTER_HEADERS_BY_REPETITION = True  # Filter repeated text across pages
PDF_FILTER_FOOTNOTES = True  # Filter page numbers and footnotes in bottom margin of pages

# PDF filtering thresholds (only used when respective filters are enabled)
PDF_HEADER_TOP_MARGIN = 0.1  # Top 10% of page considered header area
PDF_FOOTNOTE_BOTTOM_MARGIN = 0.9  # Bottom 10% of page considered footnote area
PDF_HEADER_REPETITION_THRESHOLD = 0.8  # Text must appear on 80% of pages to be considered repeated header

# ElevenLabs API configuration
ELEVENLABS_API_KEY = None  # Set this to your ElevenLabs API key or use ELEVENLABS_API_KEY environment variable
