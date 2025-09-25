<div align="center">

<img src="https://github.com/superstarryeyes/lue/blob/main/images/lue-icon.png?raw=true" alt="Lue Icon" width="50%" />

### Lue - Terminal eBook Reader with Text-to-Speech
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows%20(WSL)-lightgrey)](https://github.com/superstarryeyes/lue)
[![Terminal](https://img.shields.io/badge/interface-terminal-blue.svg)](https://github.com/superstarryeyes/lue)
[![Discord](https://img.shields.io/badge/Discord-Join%20our%20Community-5865F2?logo=discord&logoColor=white)](https://discord.gg/z8sE2gnMNk)

[Features](#-features) • [Quick Start](#-quick-start) • [Installation](#-installation) • [Usage](#-usage) • [Development](#-development)

<img src="https://github.com/superstarryeyes/lue/blob/main/images/lue-screenshot.gif" alt="Lue Screenshot" width="100%" />

</div>

---

## ✨ Features

| **Feature**                             | **Description**                                                                                |
| --------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **📖 Multi-Format Support**             | Support for EPUB, PDF, TXT, DOCX, DOC, HTML, RTF, and Markdown with seamless format detection  |
| **👄 Modular TTS System**               | Edge TTS (default) and Kokoro TTS (local/offline) with extensible architecture for new models  |
| **🌍 Cross-Platform & Multilingual**    | Full support for macOS, Linux, Windows (via WSL) with 100+ languages and consistent global experience    |
| **🎛️ Speed Adjustment**                 | Adjust text-to-speech playback speed from 1x to 3x for personalized listening experience       |
| **🎯 Precise Word Highlighting**        | Word-level highlighting synchronized with actual speech, improving focus and concentration     |
| **🌌 Rich Terminal UI**                 | Clean, responsive interface with customizable color themes and full mouse & keyboard support   |
| **💾 Smart Persistence**                | Automatic progress saving, state restoration, and cross-session continuity for seamless reading|
| **⚡️ Fast Navigation**                  | Intuitive shortcuts, flexible controls, and optional smooth scrolling for efficient book navigation     |


---

## 🚀 Quick Start

### macOS and Linux

```bash
# 1. Install FFmpeg (required for audio processing)
# macOS
brew install ffmpeg
# Ubuntu/Debian  
sudo apt install ffmpeg

# 2. Install the latest version from PyPI
pip install git+https://github.com/superstarryeyes/lue.git

# 3. Practice using Lue with the navigation guide
lue --guide

# 4. Start reading!
lue path/to/your/book.epub 
```

### Windows

**⚠️ Important:** Native Windows installation currently has compatibility issues. **Use WSL for best experience.**

```bash
# 1. Install WSL (Windows Subsystem for Linux)
# Open PowerShell as Administrator and run:
wsl --install

# 2. Restart your PC if prompted, then launch Ubuntu from Start Menu

# 3. Inside Ubuntu terminal:
sudo apt update && sudo apt upgrade -y
sudo apt install ffmpeg python3 python3-pip -y

# 4. Install Lue
pip3 install git+https://github.com/superstarryeyes/lue.git

# 5. Start reading!
lue path/to/your/book.epub
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

### Platform-Specific Setup

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

**⚠️ Windows Native Installation Issues**

Currently, Lue has compatibility issues on native Windows due to Unix-specific dependencies (`termios` module). **We strongly recommend using WSL for Windows users.**

**Option 1: WSL (Recommended)**
```bash
# 1. Install WSL
# Open PowerShell as Administrator:
wsl --install

# 2. Restart PC if prompted, launch Ubuntu from Start Menu

# 3. Follow Ubuntu installation steps above
```

**Option 2: Native Windows (Experimental)**
⚠️ **Warning:** Native Windows support is currently broken and may not work.

If you want to attempt native installation anyway:
```bash
# Download FFmpeg from ffmpeg.org and add to PATH
# Then try (but expect errors):
pip install git+https://github.com/superstarryeyes/lue.git
```

**Known Issues on Windows:**
- `ModuleNotFoundError: No module named 'termios'` - Unix-only module
- Terminal control issues
- Audio playback problems

> **💡 Help Wanted:** We're looking for contributors to help fix Windows native support! See [Contributing](#-contributing) if you're interested in helping.

### Install Lue

#### Standard Installation (macOS/Linux/WSL)

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

---

## 💻 Usage

### Basic Commands

```bash
# Start with default TTS
lue path/to/your/book.epub

# Launch without arguments to open the last book you were reading
lue

# Use specific TTS model (edge/kokoro/none) 
lue --tts kokoro path/to/your/book.epub

# Use a specific voice (full list at VOICES.md)
lue --voice "en-US-AriaNeural" path/to/your/book.epub

# Set the speech speed (e.g., 1.5x)
lue --speed 1.5 path/to/your/book.epub

# Specify a language code if needed
lue --lang a path/to/your/book.epub

# Seconds of overlap between sentences
lue --over 0.2 path/to/your/book.epub

# Enable PDF cleaning filter (removes page numbers, headers and footnotes, default: 10% (0.1) from both bottom and top of the page)
lue --filter path/to/your/book.pdf

# Set custom PDF filter margins (0.0-1.0, where 0.1 = 10% of page)
lue --filter 0.15 path/to/your/book.pdf          # Both margins to 15%
lue --filter 0.12 0.20 path/to/your/book.pdf     # Header 12%, footnote 20%

# Practice using Lue with the navigation guide
lue --guide

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
| `,` / `.`                               | Decrease or increase text-to-speech playback speed (1x to 3x)                                  |
| `s` / `w`                               | Toggle sentence highlighting or word highlighting on/off                                       |

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
- **Windows (WSL):** `~/.local/share/lue/` (within WSL filesystem)
- **Windows (Native):** `C:\Users\<User>\AppData\Local\lue\` *(if working)*

**Error Logs:**
- **macOS:** `~/Library/Logs/lue/error.log`
- **Linux:** `~/.cache/lue/log/error.log`
- **Windows (WSL):** `~/.cache/lue/log/error.log` (within WSL filesystem)
- **Windows (Native):** `C:\Users\<User>\AppData\Local\lue\Logs\error.log` *(if working)*

---

## 📄 License

This project is licensed under the **GPL-3.0 License** - see the [LICENSE](LICENSE) file for details.

---

## 🛠️ Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

**Priority Help Needed:**
- **Windows Native Support:** Fix `termios` compatibility issues and improve Windows support
- **Cross-platform Testing:** Help test on different Windows versions
- **Documentation:** Improve installation guides and troubleshooting

<div align="center">

---

*Made with 💖 for CLI enthusiasts and bookworms*

**[⭐ Star this repo](https://github.com/superstarryeyes/lue)** if you find it useful!

</div>
