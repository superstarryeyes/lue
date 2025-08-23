"""TTS implementation for ElevenLabs AI voice generation."""

import os
import asyncio
import logging
from rich.console import Console

from .base import TTSBase
from .. import config


class ElevenLabsTTS(TTSBase):
    """TTS implementation for ElevenLabs AI voice generation service."""

    @property
    def name(self) -> str:
        return "elevenlabs"

    @property
    def output_format(self) -> str:
        return "mp3"

    def __init__(self, console: Console, voice: str = None, lang: str = None):
        super().__init__(console, voice, lang)
        self.elevenlabs = None
        self.api_key = None
        
        if self.voice is None:
            self.voice = config.TTS_VOICES.get(self.name)

    async def initialize(self) -> bool:
        """Initializes the ElevenLabs TTS client."""
        try:
            import elevenlabs
            self.elevenlabs = elevenlabs
        except ImportError:
            self.console.print("[bold red]Error: 'elevenlabs' package not found.[/bold red]")
            self.console.print("[yellow]Please run 'pip install elevenlabs' to use this TTS model.[/yellow]")
            logging.error("'elevenlabs' is not installed.")
            return False

        # Get API key from environment or config
        self.api_key = os.environ.get('ELEVENLABS_API_KEY') or config.ELEVENLABS_API_KEY
        
        if not self.api_key:
            self.console.print("[bold red]Error: ElevenLabs API key not found.[/bold red]")
            self.console.print("[yellow]Please set ELEVENLABS_API_KEY environment variable or configure it in config.py[/yellow]")
            self.console.print("[cyan]You can get your API key from: https://elevenlabs.io/speech-synthesis[/cyan]")
            logging.error("ElevenLabs API key not configured.")
            return False

        # Set the API key
        self.elevenlabs.set_api_key(self.api_key)
        
        # Verify the API key works by checking available voices
        try:
            voices = await asyncio.to_thread(self.elevenlabs.voices)
            if not voices:
                self.console.print("[bold yellow]Warning: No voices found with your API key.[/bold yellow]")
                
            self.initialized = True
            self.console.print("[green]ElevenLabs TTS model initialized successfully.[/green]")
            return True
            
        except Exception as e:
            self.console.print(f"[bold red]Error: Failed to initialize ElevenLabs: {e}[/bold red]")
            self.console.print("[yellow]Please check your API key and internet connection.[/yellow]")
            logging.error(f"ElevenLabs initialization failed: {e}")
            return False

    async def generate_audio(self, text: str, output_path: str):
        """Generates audio from text using ElevenLabs and saves it to a file."""
        if not self.initialized:
            raise RuntimeError("ElevenLabs TTS has not been initialized.")
        
        if not text.strip():
            # Create empty audio file for empty text
            with open(output_path, 'wb') as f:
                f.write(b'')
            return

        try:
            # Use asyncio.to_thread to run the blocking API call in a thread
            audio_data = await asyncio.to_thread(
                self.elevenlabs.generate,
                text=text,
                voice=self.voice,
                model="eleven_monolingual_v1"
            )
            
            # Save the audio data to file
            with open(output_path, 'wb') as f:
                for chunk in audio_data:
                    if chunk:
                        f.write(chunk)
                        
        except self.elevenlabs.UnauthenticatedRateLimitError:
            self.console.print("[bold red]Error: ElevenLabs API quota exceeded or invalid API key.[/bold red]")
            self.console.print("[yellow]Please check your ElevenLabs account quota.[/yellow]")
            raise
            
        except self.elevenlabs.RateLimitError:
            self.console.print("[bold yellow]Warning: ElevenLabs rate limit exceeded. Retrying after delay...[/bold yellow]")
            await asyncio.sleep(2)  # Wait before retrying
            await self.generate_audio(text, output_path)  # Retry
            
        except Exception as e:
            logging.error(f"ElevenLabs audio generation failed for text: '{text[:50]}...'", exc_info=True)
            raise RuntimeError(f"ElevenLabs TTS failed: {e}")

    async def warm_up(self):
        """Warms up the ElevenLabs TTS model."""
        if not self.initialized:
            return

        self.console.print("[bold cyan]Warming up the ElevenLabs TTS model...[/bold cyan]")
        warmup_file = os.path.join(config.AUDIO_DATA_DIR, f".warmup_elevenlabs.{self.output_format}")
        
        try:
            await self.generate_audio("Hello, I am ready.", warmup_file)
            self.console.print("[green]ElevenLabs TTS model is ready.[/green]")
        except Exception as e:
            self.console.print(f"[bold yellow]Warning: ElevenLabs model warm-up failed: {e}[/bold yellow]")
            logging.warning(f"ElevenLabs TTS warm-up failed: {e}", exc_info=True)
        finally:
            if os.path.exists(warmup_file):
                try:
                    os.remove(warmup_file)
                except OSError:
                    pass