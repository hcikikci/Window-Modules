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
import windows_manager as wm

# Check if a window is open
is_notepad_open = wm.is_open("Notepad")  # Returns: True/False

# Focus on a specific window
wm.focus_to("Calculator")  # Returns: True if successful, False if failed

# Get active window title
current_window = wm.active_window()  # Returns: String with window title

# Get window size
calc_size = wm.size_of("Calculator")  # Returns: Tuple (width, height) or False if failed

# Center a window on screen
wm.to_center("Media Player")  # Returns: True if successful, False if failed

# Get window position
position = wm.position_of("Calculator")  # Returns: Tuple (x, y) coordinates
```

### Alternative Import Methods

1. If the file is in the same directory:

```python
import windows_manager as wm
```

2. If you want to import specific functions:

```python
from windows_manager import is_open, focus_to, active_window
```

## Functions

### `is_open(windowname)`

- **Description**: Checks if a window with the given name is open
- **Parameters**: `windowname` (str) - The title of the window to check
- **Returns**: `bool` - True if window is open, False otherwise

### `focus_to(windowname)`

- **Description**: Focuses on the specified window
- **Parameters**: `windowname` (str) - The title of the window to focus
- **Returns**: `bool` - True if successful, False if window not found

### `active_window()`

- **Description**: Returns the title of the currently active window
- **Parameters**: None
- **Returns**: `str` - Title of the active window

### `size_of(windowname)`

- **Description**: Returns the size of the specified window
- **Parameters**: `windowname` (str) - The title of the window
- **Returns**: `tuple` - (width, height) or False if window not found

### `to_center(windowname)`

- **Description**: Centers the specified window on the screen
- **Parameters**: `windowname` (str) - The title of the window to center
- **Returns**: `bool` - True if successful, False if failed

### `position_of(windowname)`

- **Description**: Returns the position of the specified window
- **Parameters**: `windowname` (str) - The title of the window
- **Returns**: `tuple` - (x, y) coordinates of the window's top-left corner

## Requirements

- Python 3.x
- pygetwindow
- pyautogui

## License

MIT License
