import pygetwindow as gw
import pyautogui as pgui

def is_open(windowname):
    """
    if window is open returns true
    example : is_open("Notepad")
    """
    windows = gw.getAllTitles()
    if windows.count(windowname) > 0:
        return True
    else:
        return False

def focus_to(windowname):
    """
    focuses on window
    example : focus_to("Notepad")
    """
    try:
        gw.getWindowsWithTitle(windowname)[0].activate()
        return True
    except:
        return False

def active_window():return gw.getActiveWindowTitle()

def size_of(windowname):
    """
    returns screen size of window
    example : size_of("Calculator")
    """
    try:
        return gw.getWindowsWithTitle(windowname)[0].size
    except:
        return False

def to_center(windowname):
    """
    change position of windowname to the center
    example : to_center("Media Player")
    """
    try:
        x = int(pgui.size()[0] / 2) - int(size_of(windowname)[0] / 2)
        y = int(pgui.size()[1] / 2) - int(size_of(windowname)[1] / 2)

        gw.getWindowsWithTitle(windowname)[0].moveTo(x,y)
        return True
    except:
        return False

def position_of(windowname):
    """
    returns position of window tuple ( x , y )
    example : position_of("Calculator")
    """
    return gw.getWindowsWithTitle(windowname)[0].topleft

