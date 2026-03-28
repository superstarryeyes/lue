"""MiniMax Cloud TTS model for the Lue eBook reader.

Uses the MiniMax Text-to-Speech API (speech-2.8-hd model) for high-quality
cloud-based speech synthesis. Requires a MINIMAX_API_KEY environment variable
and internet access.

API Reference: https://platform.minimaxi.com/document/T2A%20V2
"""

import os
import asyncio
import logging
from rich.console import Console

from .base import TTSBase
from .. import config


# Verified MiniMax voice IDs
MINIMAX_VOICES = [
    "English_Graceful_Lady",
    "English_Insightful_Speaker",
    "English_radiant_girl",
    "English_Persuasive_Man",
    "English_Lucky_Robot",
    "Wise_Woman",
    "cute_boy",
    "lovely_girl",
    "Friendly_Person",
    "Inspirational_girl",
    "Deep_Voice_Man",
    "sweet_girl",
]


class MiniMaxTTS(TTSBase):
    """TTS implementation for MiniMax Cloud Text-to-Speech API.

    Uses the speech-2.8-hd model via the /v1/t2a_v2 endpoint.
    Requires the MINIMAX_API_KEY environment variable to be set.
    """

    API_URL = "https://api.minimax.io/v1/t2a_v2"
    MODEL = "speech-2.8-hd"

    @property
    def name(self) -> str:
        return "minimax"

    @property
    def output_format(self) -> str:
        return "mp3"

    def __init__(self, console: Console, voice: str = None, lang: str = None):
        super().__init__(console, voice, lang)
        self.api_key = None
        self.requests = None

        if self.voice is None:
            self.voice = config.TTS_VOICES.get(self.name)

    async def initialize(self) -> bool:
        """Check for the requests library and a valid MINIMAX_API_KEY."""
        try:
            import requests
            self.requests = requests
        except ImportError:
            self.console.print(
                "[bold red]Error: 'requests' package not found.[/bold red]"
            )
            self.console.print(
                "[yellow]Please run 'pip install requests' to use MiniMax TTS.[/yellow]"
            )
            logging.error("'requests' is not installed for MiniMax TTS.")
            return False

        self.api_key = os.environ.get("MINIMAX_API_KEY")
        if not self.api_key:
            self.console.print(
                "[bold red]Error: MINIMAX_API_KEY environment variable not set.[/bold red]"
            )
            self.console.print(
                "[yellow]Please set MINIMAX_API_KEY to use MiniMax Cloud TTS.[/yellow]"
            )
            logging.error("MINIMAX_API_KEY is not set.")
            return False

        self.initialized = True
        self.console.print("[green]MiniMax Cloud TTS is available.[/green]")
        return True

    def _call_api(self, text: str) -> bytes:
        """Call the MiniMax TTS API and return raw MP3 audio bytes.

        Args:
            text: Text to synthesize.

        Returns:
            Raw MP3 audio bytes.

        Raises:
            RuntimeError: On API errors or unexpected responses.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.MODEL,
            "text": text,
            "voice_setting": {
                "voice_id": self.voice,
            },
            "audio_setting": {
                "format": "mp3",
            },
        }

        response = self.requests.post(
            self.API_URL, headers=headers, json=payload, timeout=60
        )
        response.raise_for_status()

        data = response.json()

        # Check for API-level errors
        if data.get("base_resp", {}).get("status_code", 0) != 0:
            error_msg = data.get("base_resp", {}).get("status_msg", "Unknown error")
            raise RuntimeError(f"MiniMax TTS API error: {error_msg}")

        audio_hex = data.get("data", {}).get("audio")
        if not audio_hex:
            raise RuntimeError("MiniMax TTS API returned no audio data.")

        return bytes.fromhex(audio_hex)

    async def generate_audio(self, text: str, output_path: str):
        """Generate audio from text using MiniMax Cloud TTS."""
        if not self.initialized:
            raise RuntimeError("MiniMax TTS has not been initialized.")

        loop = asyncio.get_running_loop()

        def _blocking_generate():
            try:
                audio_bytes = self._call_api(text)
                with open(output_path, "wb") as f:
                    f.write(audio_bytes)
            except Exception as e:
                logging.error(
                    f"MiniMax TTS audio generation failed for text: '{text[:50]}...'",
                    exc_info=True,
                )
                raise e

        await loop.run_in_executor(None, _blocking_generate)

    async def warm_up(self):
        """Warm up by making a short API request."""
        if not self.initialized:
            return

        self.console.print(
            "[bold cyan]Warming up MiniMax Cloud TTS...[/bold cyan]"
        )
        warmup_file = os.path.join(
            config.AUDIO_DATA_DIR, f".warmup_minimax.{self.output_format}"
        )
        try:
            await self.generate_audio("Ready.", warmup_file)
            self.console.print("[green]MiniMax Cloud TTS is ready.[/green]")
        except Exception as e:
            self.console.print(
                "[bold yellow]Warning: MiniMax TTS warm-up failed.[/bold yellow]"
            )
            self.console.print(
                f"[yellow]This may indicate a network issue or an invalid API key.[/yellow]"
            )
            logging.warning(f"MiniMax TTS warm-up failed: {e}", exc_info=True)
        finally:
            if os.path.exists(warmup_file):
                try:
                    os.remove(warmup_file)
                except OSError:
                    pass
