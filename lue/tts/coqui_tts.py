# lue/tts/coqui_tts.py
import os
import sys
import asyncio
import logging
from rich.console import Console
import functools
import builtins

from .base import TTSBase
from .. import config

class CoquiTTS(TTSBase):
    """
    TTS implementation for Coqui's high-quality XTTS model.
    This model runs locally on your GPU.
    """

    @property
    def name(self) -> str:
        return "coqui"

    @property
    def output_format(self) -> str:
        return "wav"

    def __init__(self, console: Console, voice: str = None, lang: str = None):
        super().__init__(console, voice, lang)
        self.model = None

        if self.voice is None:
            self.voice = config.TTS_VOICES.get(self.name)

        if self.lang is None:
            self.lang = config.TTS_LANGUAGE_CODES.get(self.name, "en")

    async def initialize(self) -> bool:
        """
        Initializes the Coqui TTS model and loads it onto the GPU, suppressing all output.
        """
        try:
            from TTS.api import TTS
            import torch
        except ImportError:
            self.console.print("[bold red]Error: 'TTS' package not found.[/bold red]")
            return False

        if not self.voice or not os.path.exists(self.voice):
            self.console.print(f"[bold red]Error: Coqui speaker file not found at '{self.voice}'[/bold red]")
            self.console.print("[yellow]Please ensure the path in config.py is correct and the voices folder is mounted.[/yellow]")
            return False

        loop = asyncio.get_running_loop()

        def _blocking_init():
            # Temporarily replace the built-in print function.
            # Some torch libraries use print for logging.
            # This can totally break the TUI session.
            original_print = builtins.print
            builtins.print = lambda *args, **kwargs: None

            model = None
            original_torch_load = torch.load
            try:
                @functools.wraps(original_torch_load)
                def unsafe_torch_load(*args, **kwargs):
                    kwargs.setdefault('weights_only', False)
                    return original_torch_load(*args, **kwargs)

                torch.load = unsafe_torch_load

                os.environ["COQUI_TOS_AGREED"] = "1"
                model_name = "tts_models/multilingual/multi-dataset/xtts_v2"

                # Use the real print for this important message
                original_print(f"[bold cyan]Loading Coqui TTS model '{model_name}' onto GPU...[/bold cyan]")

                model = TTS(model_name, gpu=True, progress_bar=False)
            except Exception as e:
                logging.error(f"Failed to initialize Coqui TTS model: {e}", exc_info=True)
            finally:
                # Restore the original print function and torch.load
                builtins.print = original_print
                torch.load = original_torch_load

            return model

        try:
            self.model = await loop.run_in_executor(None, _blocking_init)
            if self.model:
                self.initialized = True
                self.console.print("[green]Coqui TTS model loaded successfully on GPU.[/green]")
                return True
            else:
                self.console.print("[bold red]Coqui TTS model failed to initialize. Check logs for details.[/bold red]")
                return False
        except Exception as e:
            self.console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")
            return False

    async def generate_audio(self, text: str, output_path: str):
        """
        Generates audio from text using the loaded Coqui model, suppressing all output.
        """
        if not self.initialized or not self.model:
            raise RuntimeError("Coqui TTS has not been initialized.")

        def _blocking_generate():
            # Temporarily replace the built-in print function
            original_print = builtins.print
            builtins.print = lambda *args, **kwargs: None

            try:
                self.model.tts_to_file(
                    text=text,
                    file_path=output_path,
                    speaker_wav=self.voice,
                    language=self.lang
                )
            except Exception as e:
                logging.error(f"Error during Coqui audio generation for text '{text[:50]}...': {e}", exc_info=True)
                raise e
            finally:
                # Restore the original print function
                builtins.print = original_print

        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, _blocking_generate)
