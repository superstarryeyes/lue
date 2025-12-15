<div align="center">

<img src="https://github.com/superstarryeyes/lue/blob/main/images/lue-icon.png?raw=true" alt="Lue Icon" width="35%" />

### Lue - Terminal eBook Reader with Text-to-Speech
[![License: GPL v3+](https://img.shields.io/badge/License-GPLv3+-86c9fa.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/python-3.10+-86c9fa.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows%20(WSL)-86c9fa)](https://github.com/superstarryeyes/lue)
[![Terminal](https://img.shields.io/badge/interface-terminal-86c9fa.svg)](https://github.com/superstarryeyes/lue)
[![Discord](https://img.shields.io/badge/Discord-Join%20our%20Community-5865F2?logo=discord&logoColor=white)](https://discord.gg/z8sE2gnMNk)

[Features](#-features) • [Quick Start](#-quick-start-macos-and-linux) • [Installation](#-installation-macos-linux-and-windows) • [Usage](#-usage) • [Customize](#️-customize) • [Development](#-development)

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
| **🎯 Auto-Scroll & Precise Word Highlighting**        | Automatic scrolling and word-level highlighting synchronized with actual speech, improving focus and concentration     |
| **💾 Smart Persistence**                | Automatic progress saving, state restoration, and cross-session continuity for seamless reading|
| **⚡️ Fast Navigation**                  | Intuitive shortcuts, flexible controls, mouse support and optional smooth scrolling for efficient book navigation     |
| **⚙️ Extensive Customization**          | Fully customizable keyboard layouts (including Vim-style bindings), adjustable UI elements, colors, and display modes|

---

## 🚀 Quick Start (macOS and Linux)

> **Want to try Lue right away?** Follow these simple steps:

```bash
# 1. Install FFmpeg (required for audio processing)
# macOS
brew install ffmpeg
# Ubuntu/Debian  
sudo apt install ffmpeg

# 2. Install the latest version from PyPI
pip install lue-reader 

# 3. Practice using Lue with the navigation guide
lue --guide

# 4. Start reading!
lue path/to/your/book.epub 
```

> **📝 Note:** Quick start uses Edge TTS (requires internet). For offline capabilities, see [full installation](#-installation-macos-linux-and-windows).

---

## 📦 Installation (macOS, Linux and Windows)

### Prerequisites

#### Core Requirements
- **FFmpeg** - Audio processing (required)

#### Optional Dependencies  
- **espeak** - Kokoro TTS support

#### macOS (Homebrew)
```bash
brew install ffmpeg
# Optional
brew install espeak
```

#### Ubuntu/Debian
```bash
sudo apt update && sudo apt install ffmpeg
# Optional  
sudo apt install espeak
```

#### Arch Linux (AUR)
```bash
# Using yay
yay -S lue-reader-git

# Or using paru
paru -S lue-reader-git
```

#### Windows
```bash
# 1. Install WSL
# Open PowerShell as Administrator:
wsl --install

# 2. Restart your PC if prompted, then launch Ubuntu from Start Menu

# 3. Inside Ubuntu terminal:
sudo apt update && sudo apt upgrade -y
sudo apt install ffmpeg python3 python3-pip -y
# Optional  
sudo apt install espeak
```

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

# Practice Lue default keys with the navigation guide
lue --guide

# View available command line options
lue --help

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
| `r`                                     | Open the recent books menu to quickly switch between 5 last read books                       |
| `,` / `.`                               | Decrease or increase text-to-speech playback speed (1x to 3x)                                  |
| `s` / `w`                               | Toggle sentence highlighting or word highlighting on/off                                       |
| `v`                                     | Cycle through UI complexity modes (Minimal, Medium, Full)                                      |

</div>

### Mouse Controls

- **🖱️ Click** - Jump to sentence
- **🔄 Scroll** - Navigate content  
- **📍 Progress bar click** - Jump to position

## ⚙️ Customize

### UI Modes

Lue offers three UI complexity modes that you can cycle through using the `v` key or set as your default in the [config.py](lue/config.py) file:

- **Mode 0 (Minimal)** - Clean text-only display with no borders or UI elements
- **Mode 1 (Medium)** - Displays a top title bar with progress information and borders
- **Mode 2 (Full)** - Full UI with both top title bar and bottom control information

Additionally, Lue provides customizable word-level and sentence-level highlighting that can be adjusted to suit your reading preferences. You can cycle through different highlighting modes using the `w` and `s` keys. These highlighting settings can also be configured as defaults in the [config.py](lue/config.py) file.

### Keyboard Layouts

Lue comes with two built-in keyboard layouts that can be set using -k/--key command line option or set as your default in the [config.py](lue/config.py) file. You can create your own keyboard layout by copying and modifying one of the existing layout files:

- **Default Layout** - [keys_default.json](lue/keys_default.json) - Standard keyboard layout
- **Vim Layout** - [keys_vim.json](lue/keys_vim.json) - Vim-style keyboard layout
- **Custom Layout** - Customize your own navigation keys by creating your own keyboard layout json file

### Color Themes

Lue allows you to customize the color theme, visual icons/symbols and all ui elements of the interface by modifying the classes in [ui.py](lue/ui.py). Create your own theme or choose one of the three themes that come with the default installation.

- **Default Theme** - The default colorful theme with various colors for different UI elements
- **Black Theme** - A dark monochrome theme that's suitable for bright backgrounds
- **White Theme** - A light monochrome theme that's suitable for dark backgrounds

---

## 🧩 Development

> **Interested in extending Lue?** 

Check out the [Developer Guide](DEVELOPER.md) for instructions on adding new TTS models and contributing to the project.

### Data Storage

**Reading Progress:**
- **macOS:** `~/Library/Application Support/lue/`
- **Linux:** `~/.local/share/lue/`  
- **Windows (WSL):** `~/.local/share/lue/` (within WSL filesystem)

**Error Logs:**
- **macOS:** `~/Library/Logs/lue/error.log`
- **Linux:** `~/.cache/lue/log/error.log`
- **Windows (WSL):** `~/.cache/lue/log/error.log` (within WSL filesystem)

---

## 🛠️ Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

Join our Discord community for discussions, support and collaboration for creating modules for new TTS models!

[![Join our Discord](https://img.shields.io/badge/Discord-Join%20Us-5865F2?logo=discord&style=for-the-badge)](https://discord.gg/z8sE2gnMNk)

---

## 📄 License

This project is licensed under the **GPL-3.0-or-later License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<a title="This tool is Tool of The Week on Terminal Trove, The $HOME of all things in the terminal" href="https://terminaltrove.com/"><img src="https://cdn.terminaltrove.com/media/badges/tool_of_the_week/png/terminal_trove_tool_of_the_week_gold_transparent.png" width="40%" alt="Terminal Trove Tool of The Week" /></a>

*Made with 💖 for CLI enthusiasts and bookworms*

**⭐ Star this repo** if you find it useful!

</div>
