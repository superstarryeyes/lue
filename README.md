<div align="center">

<img src="https://github.com/superstarryeyes/lue/blob/main/images/lue-icon.png?raw=true" alt="Lue Icon" width="35%" />

### Lue - Terminal eBook Reader with Text-to-Speech
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)](https://github.com/superstarryeyes/lue)
[![Terminal](https://img.shields.io/badge/interface-terminal-blue.svg)](https://github.com/superstarryeyes/lue)
[![Discord](https://img.shields.io/badge/Discord-Join%20our%20Community-5865F2?logo=discord&logoColor=white)](https://discord.gg/z8sE2gnMNk)

[Features](#-features) • [Quick Start](#-quick-start) • [Installation](#-installation) • [Usage](#-usage) • [Customize](#-customize) • [Development](#-development)

<img src="https://github.com/superstarryeyes/lue/blob/main/images/lue-screenshot.gif" alt="Lue Screenshot" width="100%" />

</div>

---

## ✨ Features

| **Feature**                             | **Description**                                                                                |
| --------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **📖 Multi-Format Support**             | Support for EPUB, PDF, TXT, DOCX, DOC, HTML, RTF, and Markdown with seamless format detection  |
| **👄 Modular TTS System**               | Edge TTS (default) and Kokoro TTS (local/offline) with extensible architecture for new models  |
| **🌍 Cross-Platform & Multilingual**    | Full support for macOS, Linux, Windows with 100+ languages and consistent global experience    |
| **🎛️ Speed Adjustment**                 | Adjust text-to-speech playback speed from 1x to 3x for personalized listening experience       |
| **🎯 Precise Word Highlighting**        | Word-level highlighting synchronized with actual speech, improving focus and concentration     |
| **🌌 Rich Terminal UI**                 | Clean, responsive interface with customizable color themes and full mouse & keyboard support   |
| **💾 Smart Persistence**                | Automatic progress saving, state restoration, and cross-session continuity for seamless reading|
| **⚡️ Fast Navigation**                  | Intuitive shortcuts, flexible controls, and optional smooth scrolling for efficient book navigation     |


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

# 2. Install the latest version from PyPI
pip install lue-reader 

# 3. Practice using Lue with the navigation guide
lue --guide

# 4. Start reading!
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

# Use the Vim keyboard layout
lue --keys vim path/to/your/book.epub

# Practice using Lue with the navigation guide
lue --guide

# View available options
lue --help
```

### Keyboard Controls (Default)

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
| `v`                                     | Cycle through UI complexity modes (Minimal, Medium, Full)                                      |

</div>

### Mouse Controls

- **🖱️ Click** - Jump to sentence
- **🔄 Scroll** - Navigate content  
- **📍 Progress bar click** - Jump to position

## 🎨 Customize

Lue offers extensive customization options for both the user interface and keyboard shortcuts to match your preferences and workflow.

### UI Modes

Lue offers three UI complexity modes that you can cycle through using the `v` key or set as your default in the [config.py](lue/config.py) file:

- **Mode 0 (Minimal)** - Clean text-only display with no borders or UI elements
- **Mode 1 (Medium)** - Displays a top title bar with progress information and borders
- **Mode 2 (Full)** - Full UI with both top title bar and bottom control information

### Keyboard Layouts

Lue comes with two built-in keyboard layouts that can be set using -k/--key command line option or set as your default in the [config.py](lue/config.py) file. You can create your own keyboard layout by copying and modifying one of the existing layout files:

- **Default Layout** - [keys_default.json](lue/keys_default.json) - Standard keyboard layout
- **Vim Layout** - [keys_vim.json](lue/keys_vim.json) - Vim-style keyboard layout
- **Custom Layout** - Customize your own navigation keys by creating your own keyboard layout json file.

Custom layouts must follow the same JSON structure as the built-in layouts, with sections for navigation, TTS controls, display controls, and application controls.

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

<a title="This tool is Tool of The Week on Terminal Trove, The $HOME of all things in the terminal" href="https://terminaltrove.com/"><img src="https://cdn.terminaltrove.com/media/badges/tool_of_the_week/png/terminal_trove_tool_of_the_week_gold_transparent.png" width="40%" alt="Terminal Trove Tool of The Week" /></a>

*Made with 💖 for CLI enthusiasts and bookworms*

**[⭐ Star this repo](https://github.com/superstarryeyes/lue)** if you find it useful!

</div>
