import sys
import select
import asyncio
import subprocess
import json
import os

# Default keyboard shortcuts
DEFAULT_KEYBOARD_SHORTCUTS = {
    "navigation": {
        "next_paragraph": "l",
        "prev_paragraph": "h",
        "next_sentence": "k",
        "prev_sentence": "j",
        "scroll_page_up": "i",
        "scroll_page_down": "m",
        "scroll_up": "u",
        "scroll_down": "n",
        "move_to_top_visible": "t",
        "move_to_beginning": "y",
        "move_to_end": "b"
    },
    "tts_controls": {
        "play_pause": "p",
        "decrease_speed": ",",
        "increase_speed": ".",
        "toggle_sentence_highlight": "s",
        "toggle_word_highlight": "w"
    },
    "display_controls": {
        "toggle_auto_scroll": "a",
        "cycle_ui_complexity": "v"
    },
    "application": {
        "quit": "q"
    }
}

# Global variable to store loaded keyboard shortcuts
KEYBOARD_SHORTCUTS = DEFAULT_KEYBOARD_SHORTCUTS

def load_keyboard_shortcuts(file_path=None):
    """Load keyboard shortcuts from a JSON file or use defaults.
    
    If file_path is None, the function will attempt to load from the default locations.
    """
    global KEYBOARD_SHORTCUTS
    
    # If no file path provided, use the default file
    if not file_path:
        file_path = os.path.join(os.path.dirname(__file__), 'keys_default.json')
    
    try:
        with open(file_path, 'r') as f:
            KEYBOARD_SHORTCUTS = json.load(f)
    except Exception:
        # Fallback to default shortcuts if file cannot be loaded
        KEYBOARD_SHORTCUTS = DEFAULT_KEYBOARD_SHORTCUTS

def process_input(reader):
    """Process user input from stdin."""
    try:
        if select.select([sys.stdin], [], [], 0)[0]:
            data = sys.stdin.read(1)
            
            if not data:
                return
            
            if data == '\x1b':
                reader.mouse_sequence_buffer = data
                reader.mouse_sequence_active = True
                return
            elif reader.mouse_sequence_active:
                reader.mouse_sequence_buffer += data
                
                if reader.mouse_sequence_buffer.startswith('\x1b[<') and (data == 'M' or data == 'm'):
                    sequence = reader.mouse_sequence_buffer
                    reader.mouse_sequence_buffer = ''
                    reader.mouse_sequence_active = False
                    
                    if len(sequence) > 3:
                        mouse_part = sequence[3:]
                        if mouse_part.endswith('M') or mouse_part.endswith('m'):
                            try:
                                parts = mouse_part[:-1].split(';')
                                if len(parts) >= 3:
                                    button = int(parts[0])
                                    x_pos = int(parts[1])
                                    y_pos = int(parts[2])
                                    
                                    if mouse_part.endswith('M'):
                                        if button == 0:
                                            if reader._is_click_on_progress_bar(x_pos, y_pos):
                                                if reader._handle_progress_bar_click(x_pos, y_pos):
                                                    return
                                            
                                            if not reader._is_click_on_text(x_pos, y_pos):
                                                return

                                            # Cancel any pending restart task before killing audio
                                            if hasattr(reader, 'pending_restart_task') and reader.pending_restart_task and not reader.pending_restart_task.done():
                                                reader.pending_restart_task.cancel()
                                            
                                            _kill_audio_immediately(reader)
                                            reader.loop.call_soon_threadsafe(reader._post_command_sync, ('click_jump', (x_pos, y_pos)))
                                        elif button == 64:
                                            if reader.auto_scroll_enabled:
                                                reader.auto_scroll_enabled = False
                                            reader.loop.call_soon_threadsafe(reader._post_command_sync, 'wheel_scroll_up')
                                        elif button == 65:
                                            if reader.auto_scroll_enabled:
                                                reader.auto_scroll_enabled = False
                                            reader.loop.call_soon_threadsafe(reader._post_command_sync, 'wheel_scroll_down')
                                    return
                            except (ValueError, IndexError):
                                pass
                    return
                
                elif reader.mouse_sequence_buffer.startswith('\x1b[') and len(reader.mouse_sequence_buffer) >= 3 and data in 'ABCD':
                    sequence = reader.mouse_sequence_buffer
                    reader.mouse_sequence_buffer = ''
                    reader.mouse_sequence_active = False
                    
                    _kill_audio_immediately(reader)
                    cmd = None
                    if data == 'C':
                        cmd = 'next_sentence'
                    elif data == 'D':
                        cmd = 'prev_sentence'
                    elif data == 'B':
                        cmd = 'next_paragraph'
                    elif data == 'A':
                        cmd = 'prev_paragraph'
                    
                    if cmd:
                        reader.loop.call_soon_threadsafe(reader._post_command_sync, cmd)
                    return
                
                return
            
            reader.mouse_sequence_buffer = ''
            reader.mouse_sequence_active = False
            
            # Get keyboard shortcuts
            nav_shortcuts = KEYBOARD_SHORTCUTS.get("navigation", {})
            tts_shortcuts = KEYBOARD_SHORTCUTS.get("tts_controls", {})
            display_shortcuts = KEYBOARD_SHORTCUTS.get("display_controls", {})
            app_shortcuts = KEYBOARD_SHORTCUTS.get("application", {})
            
            # Map input data to commands using loaded shortcuts
            if data == app_shortcuts.get("quit", "q"):
                reader.running = False
                reader.command_received_event.set()
                return
            
            cmd = None
            if data == tts_shortcuts.get("play_pause", "p"):
                cmd = 'pause'
            elif data == nav_shortcuts.get("prev_paragraph", "h"):
                cmd = 'prev_paragraph'
            elif data == nav_shortcuts.get("prev_sentence", "j"):
                cmd = 'prev_sentence'
            elif data == nav_shortcuts.get("next_sentence", "k"):
                cmd = 'next_sentence'
            elif data == nav_shortcuts.get("next_paragraph", "l"):
                cmd = 'next_paragraph'
            elif data == nav_shortcuts.get("scroll_page_up", "i"):
                cmd = 'scroll_page_up'
            elif data == nav_shortcuts.get("scroll_page_down", "m"):
                cmd = 'scroll_page_down'
            elif data == nav_shortcuts.get("scroll_up", "u"):
                cmd = 'scroll_up'
            elif data == nav_shortcuts.get("scroll_down", "n"):
                cmd = 'scroll_down'
            elif data == display_shortcuts.get("toggle_auto_scroll", "a"):
                cmd = 'toggle_auto_scroll'
            elif data == nav_shortcuts.get("move_to_top_visible", "t"):
                cmd = 'move_to_top_visible'
            elif data == nav_shortcuts.get("move_to_beginning", "y"):
                cmd = 'move_to_beginning'
            elif data == nav_shortcuts.get("move_to_end", "b"):
                cmd = 'move_to_end'
            elif data == tts_shortcuts.get("decrease_speed", ","):
                cmd = 'decrease_speed'
            elif data == tts_shortcuts.get("increase_speed", "."):
                cmd = 'increase_speed'
            elif data == tts_shortcuts.get("toggle_sentence_highlight", "s"):
                cmd = 'toggle_sentence_highlight'
            elif data == tts_shortcuts.get("toggle_word_highlight", "w"):
                cmd = 'toggle_word_highlight'
            elif data == display_shortcuts.get("cycle_ui_complexity", "v"):
                cmd = 'cycle_ui_complexity'
            
            if cmd:
                reader.loop.call_soon_threadsafe(reader._post_command_sync, cmd)
                
    except Exception:
        pass

def _kill_audio_immediately(reader):
    """Kill audio playback immediately."""
    for process in reader.playback_processes[:]:
        try:
            process.kill()
        except (ProcessLookupError, AttributeError):
            pass
    try:
        subprocess.run(['pkill', '-f', 'ffplay'], check=False, 
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass