<div align="center">

<img src="https://github.com/superstarryeyes/lue/blob/main/images/logo.png?raw=true" alt="Lue Logo" width="70%" />

### Lue - Terminal eBook Reader with Text-to-Speech

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)](https://github.com/superstarryeyes/lue)
[![Terminal](https://img.shields.io/badge/interface-terminal-blue.svg)](https://github.com/superstarryeyes/lue)
[![Discord](https://img.shields.io/badge/Discord-Join%20our%20Community-5865F2?logo=discord&logoColor=white)](https://discord.gg/xynDDqsm)

[Features](#-features) • [Quick Start](#-quick-start) • [Installation](#-installation) • [Usage](#-usage) • [Development](#-development)

<img src="https://github.com/superstarryeyes/lue/blob/main/images/screenshot.png" alt="Lue Screenshot" width="100%" />

</div>

---

## ✨ Features

| **Feature**                             | **Description**                                                                                |
| --------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **📖 Multi-Format Support**             | Support for EPUB, PDF, TXT, DOCX, DOC, HTML, RTF, and Markdown with seamless format detection  |
| **👄 Modular TTS System**               | Edge TTS (default), ElevenLabs TTS (AI voices), and Kokoro TTS (local/offline) with extensible architecture |
| **🌌 Rich Terminal UI**                 | Clean, responsive interface with customizable color themes and full mouse & keyboard support   |
| **💾 Smart Persistence**                | Automatic progress saving, state restoration, and cross-session continuity for seamless reading|
| **🌍 Cross-Platform & Multilingual**    | Full support for macOS, Linux, Windows with 100+ languages and consistent global experience    |
| **⚡️ Fast Navigation**                  | Intuitive shortcuts, flexible controls, and smooth scrolling for efficient book navigation     |

---

## 🚀 Quick Start

> **Want to try Lue right away?** Follow these simple steps:

```bash
# 1. Install FFmpeg (required for audio processing)
# macOS
brew install ffmpeg
# Ubuntu/Debian  
sudo apt install ffmpeg
# Windows: Download from ffmpeg.org and add to PATH

# 2. Clone and setup
git clone https://github.com/superstarryeyes/lue.git
cd lue
pip install -r requirements.txt

# 3. Start reading!
python -m lue sample.txt
```

> **📝 Note:** Quick start uses Edge TTS (requires internet). For offline capabilities, see [full installation](#-installation).

---

## 📦 Installation

### Prerequisites

#### Core Requirements
- **FFmpeg** - Audio processing (required)

#### Optional Dependencies  
- **espeak** - Kokoro TTS support
- **antiword** - .doc file support

#### macOS (Homebrew)
```bash
brew install ffmpeg
# Optional
brew install espeak antiword
```

#### Ubuntu/Debian
```bash
sudo apt update && sudo apt install ffmpeg
# Optional  
sudo apt install espeak antiword
```

#### Windows
Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.

### Install Lue

#### Standard Installation

```bash
# 1. Clone repository
git clone https://github.com/superstarryeyes/lue.git
cd lue

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install Lue
pip install .
```

#### Enable Kokoro TTS (Optional)

For local/offline TTS capabilities:

```bash
# 1. Edit requirements.txt - uncomment Kokoro packages:
kokoro>=0.9.4
soundfile>=0.13.1
huggingface-hub>=0.34.4

# 2. Install PyTorch
# CPU version:
pip install torch torchvision torchaudio
# GPU version (CUDA):
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# 3. Install updated requirements
pip install -r requirements.txt

# 4. Install Lue
pip install .
```

#### Enable ElevenLabs TTS (Optional)

For high-quality AI voice synthesis:

```bash
# 1. Install ElevenLabs package
pip install elevenlabs

# 2. Set your API key (get it from https://elevenlabs.io/speech-synthesis)
export ELEVENLABS_API_KEY="your_api_key_here"

# Or alternatively, set it in config.py:
# ELEVENLABS_API_KEY = "your_api_key_here"
```

---

## 💻 Usage

### Basic Commands

```bash
# Start with default TTS
lue path/to/your/book.epub

# Use specific TTS model  
lue --tts kokoro path/to/your/book.epub
lue --tts elevenlabs path/to/your/book.epub

# Use a specific voice (full list at VOICES.md)
lue --voice "en-US-AriaNeural" path/to/your/book.epub

# Specify a language code if needed
lue --lang a path/to/your/book.epub

# Seconds of overlap between sentences
lue --over 0.2 path/to/your/book.epub

# Enable PDF cleaning filter (removes page numbers, headers and footnotes)
lue --filter path/to/your/book.pdf

# View available options
lue --help
```

### Keyboard Controls

<div align="center">

| **Key Binding**                         | **Action Description**                                                                         |
| --------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `q`                                     | Quit the application and save current reading progress automatically                           |
| `p`                                     | Pause or resume the text-to-speech audio playback                                              |
| `a`                                     | Toggle auto-scroll mode to automatically advance during TTS playback                           |
| `t`                                     | Select and highlight the top sentence of the current visible page                              |
| `h` / `l`                               | Move the reading line to the previous or next paragraph in the document                        |
| `j` / `k`                               | Move the reading line to the previous or next sentence in the document                         |
| `i` / `m`                               | Jump up or down by full pages for rapid navigation through longer documents                    |
| `u` / `n`                               | Scroll up or down by smaller increments for fine-grained position control                      |
| `y` / `b`                               | Jump directly to the beginning or end of the document for quick navigation                     |

</div>

### Mouse Controls

- **🖱️ Click** - Jump to sentence
- **🔄 Scroll** - Navigate content  
- **📍 Progress bar click** - Jump to position

---

## 🧩 Development

> **Interested in extending Lue?** 

Check out the [Developer Guide](DEVELOPER.md) for instructions on adding new TTS models and contributing to the project.

### Data Storage

**Reading Progress:**
- **macOS:** `~/Library/Application Support/lue/`
- **Linux:** `~/.local/share/lue/`  
- **Windows:** `C:\Users\<User>\AppData\Local\lue\`

**Error Logs:**
- **macOS:** `~/Library/Logs/lue/error.log`
- **Linux:** `~/.cache/lue/log/error.log`
- **Windows:** `C:\Users\<User>\AppData\Local\lue\Logs\error.log`

---

## 📄 License

This project is licensed under the **GPL-3.0 License** - see the [LICENSE](LICENSE) file for details.

---

## 🛠️ Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

<div align="center">

---

*Made with 💖 for CLI enthusiasts and bookworms*

**[⭐ Star this repo](https://github.com/superstarryeyes/lue)** if you find it useful!

</div>
