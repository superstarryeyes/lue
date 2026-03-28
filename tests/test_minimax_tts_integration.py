"""Integration tests for MiniMax Cloud TTS provider.

These tests call the real MiniMax TTS API and require:
  - MINIMAX_API_KEY environment variable to be set
  - Network access to api.minimax.io

Skip automatically when the API key is not available.
"""

import asyncio
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

MINIMAX_API_KEY = os.environ.get("MINIMAX_API_KEY")
SKIP_REASON = "MINIMAX_API_KEY not set; skipping live API tests"


@unittest.skipUnless(MINIMAX_API_KEY, SKIP_REASON)
class TestMiniMaxTTSIntegration(unittest.TestCase):
    """Live integration tests against the MiniMax TTS API."""

    def setUp(self):
        from unittest.mock import MagicMock
        from lue.tts.minimax_tts import MiniMaxTTS

        self.console = MagicMock()
        self.tts = MiniMaxTTS(self.console)
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        initialized = self.loop.run_until_complete(self.tts.initialize())
        self.assertTrue(initialized, "MiniMax TTS should initialize with valid API key")

    def tearDown(self):
        self.loop.close()

    def test_generate_short_text(self):
        """Should generate a valid MP3 file from short text."""
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            output_path = f.name

        try:
            self.loop.run_until_complete(
                self.tts.generate_audio("Hello, world.", output_path)
            )
            self.assertTrue(os.path.exists(output_path))
            size = os.path.getsize(output_path)
            self.assertGreater(size, 100, "MP3 file should be non-trivial")

            # Verify it looks like an MP3 (check for common MP3 signatures)
            with open(output_path, "rb") as f:
                header = f.read(4)
            # MP3 files typically start with 0xFF 0xFB or ID3 tag
            is_mp3 = header[:2] == b"\xff\xfb" or header[:3] == b"ID3"
            self.assertTrue(is_mp3, f"File should be MP3, got header: {header.hex()}")
        finally:
            os.unlink(output_path)

    def test_generate_with_custom_voice(self):
        """Should generate audio with a different voice."""
        from unittest.mock import MagicMock
        from lue.tts.minimax_tts import MiniMaxTTS

        tts = MiniMaxTTS(MagicMock(), voice="Deep_Voice_Man")
        self.loop.run_until_complete(tts.initialize())

        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            output_path = f.name

        try:
            self.loop.run_until_complete(
                tts.generate_audio("Testing with a deep voice.", output_path)
            )
            self.assertTrue(os.path.exists(output_path))
            self.assertGreater(os.path.getsize(output_path), 100)
        finally:
            os.unlink(output_path)

    def test_warm_up(self):
        """Warm-up should complete without error."""
        self.loop.run_until_complete(self.tts.warm_up())


if __name__ == "__main__":
    unittest.main()
