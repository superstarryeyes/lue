"""Unit tests for MiniMax Cloud TTS provider."""

import json
import os
import sys
import asyncio
import unittest
from unittest.mock import MagicMock, patch, PropertyMock

# Add parent directory to path so we can import lue modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lue.tts.minimax_tts import MiniMaxTTS, MINIMAX_VOICES
from lue.tts.base import TTSBase


class TestMiniMaxTTSProperties(unittest.TestCase):
    """Test MiniMaxTTS class properties and constants."""

    def setUp(self):
        self.console = MagicMock()
        self.tts = MiniMaxTTS(self.console)

    def test_name(self):
        self.assertEqual(self.tts.name, "minimax")

    def test_output_format(self):
        self.assertEqual(self.tts.output_format, "mp3")

    def test_inherits_tts_base(self):
        self.assertIsInstance(self.tts, TTSBase)

    def test_api_url(self):
        self.assertEqual(
            MiniMaxTTS.API_URL, "https://api.minimax.io/v1/t2a_v2"
        )

    def test_model_name(self):
        self.assertEqual(MiniMaxTTS.MODEL, "speech-2.8-hd")

    def test_default_voice_from_config(self):
        """Default voice should come from config when none provided."""
        tts = MiniMaxTTS(self.console)
        self.assertEqual(tts.voice, "English_Graceful_Lady")

    def test_custom_voice(self):
        """Custom voice should override default."""
        tts = MiniMaxTTS(self.console, voice="Deep_Voice_Man")
        self.assertEqual(tts.voice, "Deep_Voice_Man")

    def test_voices_list(self):
        """All verified voice IDs should be in the list."""
        self.assertIn("English_Graceful_Lady", MINIMAX_VOICES)
        self.assertIn("Deep_Voice_Man", MINIMAX_VOICES)
        self.assertIn("sweet_girl", MINIMAX_VOICES)
        self.assertEqual(len(MINIMAX_VOICES), 12)


class TestMiniMaxTTSInitialize(unittest.TestCase):
    """Test MiniMaxTTS initialization."""

    def setUp(self):
        self.console = MagicMock()

    def test_initialize_missing_requests(self):
        """Should fail gracefully when requests is not installed."""
        tts = MiniMaxTTS(self.console)
        with patch.dict("sys.modules", {"requests": None}):
            with patch("builtins.__import__", side_effect=ImportError("No module named 'requests'")):
                result = asyncio.get_event_loop().run_until_complete(
                    tts.initialize()
                )
        self.assertFalse(result)
        self.assertFalse(tts.initialized)

    def test_initialize_missing_api_key(self):
        """Should fail when MINIMAX_API_KEY is not set."""
        tts = MiniMaxTTS(self.console)
        with patch.dict(os.environ, {}, clear=True):
            # Ensure MINIMAX_API_KEY is not set
            os.environ.pop("MINIMAX_API_KEY", None)
            result = asyncio.get_event_loop().run_until_complete(
                tts.initialize()
            )
        self.assertFalse(result)
        self.assertFalse(tts.initialized)

    def test_initialize_success(self):
        """Should succeed when requests is available and API key is set."""
        tts = MiniMaxTTS(self.console)
        with patch.dict(os.environ, {"MINIMAX_API_KEY": "test-key-123"}):
            result = asyncio.get_event_loop().run_until_complete(
                tts.initialize()
            )
        self.assertTrue(result)
        self.assertTrue(tts.initialized)
        self.assertEqual(tts.api_key, "test-key-123")

    def test_initialize_stores_api_key(self):
        """API key should be stored for later use."""
        tts = MiniMaxTTS(self.console)
        with patch.dict(os.environ, {"MINIMAX_API_KEY": "my-secret-key"}):
            asyncio.get_event_loop().run_until_complete(tts.initialize())
        self.assertEqual(tts.api_key, "my-secret-key")


class TestMiniMaxTTSCallAPI(unittest.TestCase):
    """Test the _call_api method."""

    def setUp(self):
        self.console = MagicMock()
        self.tts = MiniMaxTTS(self.console)
        self.tts.api_key = "test-key"
        self.tts.initialized = True

        import requests
        self.tts.requests = requests

    @patch("requests.post")
    def test_call_api_success(self, mock_post):
        """Should return decoded audio bytes on success."""
        # "hello" in hex
        audio_hex = b"hello world".hex()
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "base_resp": {"status_code": 0},
            "data": {"audio": audio_hex},
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        result = self.tts._call_api("Test text")
        self.assertEqual(result, b"hello world")

        # Verify API call
        mock_post.assert_called_once()
        call_kwargs = mock_post.call_args
        self.assertIn("Authorization", call_kwargs.kwargs.get("headers", call_kwargs[1].get("headers", {})))

    @patch("requests.post")
    def test_call_api_sends_correct_payload(self, mock_post):
        """Should send correct model, voice, and format."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "base_resp": {"status_code": 0},
            "data": {"audio": "aabb"},
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        self.tts._call_api("Hello")

        call_args = mock_post.call_args
        payload = call_args.kwargs.get("json", call_args[1].get("json", {}))
        self.assertEqual(payload["model"], "speech-2.8-hd")
        self.assertEqual(payload["text"], "Hello")
        self.assertEqual(
            payload["voice_setting"]["voice_id"], "English_Graceful_Lady"
        )
        self.assertEqual(payload["audio_setting"]["format"], "mp3")

    @patch("requests.post")
    def test_call_api_error_status(self, mock_post):
        """Should raise RuntimeError on API error status."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "base_resp": {
                "status_code": 1001,
                "status_msg": "Invalid API key",
            },
            "data": {},
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        with self.assertRaises(RuntimeError) as ctx:
            self.tts._call_api("Test")
        self.assertIn("Invalid API key", str(ctx.exception))

    @patch("requests.post")
    def test_call_api_no_audio_data(self, mock_post):
        """Should raise RuntimeError when no audio data returned."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "base_resp": {"status_code": 0},
            "data": {},
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        with self.assertRaises(RuntimeError) as ctx:
            self.tts._call_api("Test")
        self.assertIn("no audio data", str(ctx.exception))

    @patch("requests.post")
    def test_call_api_http_error(self, mock_post):
        """Should propagate HTTP errors."""
        import requests
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.HTTPError(
            "500 Server Error"
        )
        mock_post.return_value = mock_response

        with self.assertRaises(requests.HTTPError):
            self.tts._call_api("Test")

    @patch("requests.post")
    def test_call_api_bearer_auth(self, mock_post):
        """Should use Bearer token authentication."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "base_resp": {"status_code": 0},
            "data": {"audio": "aabb"},
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        self.tts._call_api("Test")

        call_args = mock_post.call_args
        headers = call_args.kwargs.get("headers", call_args[1].get("headers", {}))
        self.assertEqual(headers["Authorization"], "Bearer test-key")


class TestMiniMaxTTSGenerateAudio(unittest.TestCase):
    """Test generate_audio method."""

    def setUp(self):
        self.console = MagicMock()
        self.tts = MiniMaxTTS(self.console)
        self.tts.api_key = "test-key"
        self.tts.initialized = True

        import requests
        self.tts.requests = requests

    def test_generate_audio_not_initialized(self):
        """Should raise RuntimeError when not initialized."""
        tts = MiniMaxTTS(self.console)
        with self.assertRaises(RuntimeError):
            asyncio.get_event_loop().run_until_complete(
                tts.generate_audio("Test", "/tmp/test.mp3")
            )

    @patch("requests.post")
    def test_generate_audio_writes_file(self, mock_post):
        """Should write audio bytes to the output file."""
        audio_bytes = b"\xff\xfb\x90\x00"  # Fake MP3 header
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "base_resp": {"status_code": 0},
            "data": {"audio": audio_bytes.hex()},
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            output_path = f.name

        try:
            asyncio.get_event_loop().run_until_complete(
                self.tts.generate_audio("Test text", output_path)
            )
            with open(output_path, "rb") as f:
                written = f.read()
            self.assertEqual(written, audio_bytes)
        finally:
            os.unlink(output_path)


class TestMiniMaxTTSWarmUp(unittest.TestCase):
    """Test warm_up method."""

    def setUp(self):
        self.console = MagicMock()
        self.tts = MiniMaxTTS(self.console)
        self.tts.api_key = "test-key"
        self.tts.initialized = True

        import requests
        self.tts.requests = requests

    def test_warm_up_not_initialized(self):
        """Should silently return when not initialized."""
        tts = MiniMaxTTS(self.console)
        # Should not raise
        asyncio.get_event_loop().run_until_complete(tts.warm_up())

    @patch("requests.post")
    def test_warm_up_success(self, mock_post):
        """Should complete without error on success."""
        audio_bytes = b"\xff\xfb\x90\x00"
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "base_resp": {"status_code": 0},
            "data": {"audio": audio_bytes.hex()},
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        asyncio.get_event_loop().run_until_complete(self.tts.warm_up())

    @patch("requests.post")
    def test_warm_up_failure_handled(self, mock_post):
        """Should handle warm-up failure gracefully."""
        mock_post.side_effect = Exception("Network error")

        # Should not raise
        asyncio.get_event_loop().run_until_complete(self.tts.warm_up())


class TestMiniMaxTTSAutoDiscovery(unittest.TestCase):
    """Test that MiniMax TTS is discoverable by TTSManager."""

    def test_module_follows_naming_convention(self):
        """File must be named *_tts.py for auto-discovery."""
        tts_dir = os.path.join(
            os.path.dirname(__file__), "..", "lue", "tts"
        )
        minimax_file = os.path.join(tts_dir, "minimax_tts.py")
        self.assertTrue(
            os.path.exists(minimax_file),
            "minimax_tts.py must exist in lue/tts/ for auto-discovery",
        )

    def test_tts_manager_discovers_minimax(self):
        """TTSManager should discover the minimax model."""
        from lue.tts_manager import TTSManager

        manager = TTSManager()
        available = manager.get_available_tts_names()
        self.assertIn("minimax", available)

    def test_tts_manager_creates_minimax(self):
        """TTSManager should be able to create a MiniMax instance."""
        from lue.tts_manager import TTSManager

        manager = TTSManager()
        console = MagicMock()
        model = manager.create_model("minimax", console)
        self.assertIsNotNone(model)
        self.assertIsInstance(model, MiniMaxTTS)
        self.assertEqual(model.name, "minimax")


class TestMiniMaxTTSConfig(unittest.TestCase):
    """Test MiniMax entries in config.py."""

    def test_default_voice_in_config(self):
        from lue import config

        self.assertIn("minimax", config.TTS_VOICES)
        self.assertEqual(
            config.TTS_VOICES["minimax"], "English_Graceful_Lady"
        )


if __name__ == "__main__":
    unittest.main()
