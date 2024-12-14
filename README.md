# python-windows-manager

A Python utility library for managing and controlling window operations in Windows OS.

## Features

- Check if a window is open
- Focus on specific windows
- Get active window information
- Get window size
- Center windows on screen
- Get window position

## Installation

```bash
pip install pygetwindow
pip install pyautogui
```

## Usage

```python
import Window_Modules as wm

# Check if a window is open
is_notepad_open = wm.is_open("Notepad")

# Focus on a specific window
wm.focus_to("Calculator")

# Get active window title
current_window = wm.active_window()

# Get window size
calc_size = wm.size_of("Calculator")

# Center a window on screen
wm.to_center("Media Player")

# Get window position
position = wm.position_of("Calculator")
```

## Functions

- `is_open(windowname)`: Checks if a window with the given name is open
- `focus_to(windowname)`: Focuses on the specified window
- `active_window()`: Returns the title of the currently active window
- `size_of(windowname)`: Returns the size of the specified window
- `to_center(windowname)`: Centers the specified window on the screen
- `position_of(windowname)`: Returns the position (x, y) of the specified window

## Requirements

- Python 3.x
- pygetwindow
- pyautogui

## License

MIT License
