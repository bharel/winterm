import ctypes
from ctypes import wintypes

__all__ = ["enable", "disable", "is_enabled"]

STD_OUTPUT_HANDLE = -11
ENABLE_PROCESSED_OUTPUT = 1
ENABLE_VIRTUAL_TERMINAL_PROCESSING = 4

ENABLE_VIRTUAL_TERMINAL = (
    ENABLE_VIRTUAL_TERMINAL_PROCESSING | ENABLE_PROCESSED_OUTPUT)

def errcheck(result, func, args):
    if not result:
        raise ctypes.WinError()
    return args

GetStdHandle = ctypes.windll.kernel32.GetStdHandle
GetStdHandle.argtypes = [wintypes.DWORD]
GetStdHandle.restype = wintypes.HANDLE
GetStdHandle.errcheck = errcheck

GetConsoleMode = ctypes.windll.kernel32.GetConsoleMode
GetConsoleMode.argtypes = [wintypes.HANDLE, wintypes.LPDWORD]
GetConsoleMode.restype = wintypes.BOOL
GetConsoleMode.errcheck = errcheck

SetConsoleMode = ctypes.windll.kernel32.SetConsoleMode
SetConsoleMode.argtypes = [wintypes.HANDLE, wintypes.DWORD]
SetConsoleMode.restype = wintypes.BOOL
SetConsoleMode.errcheck = errcheck

def _get_stdout_handle() -> wintypes.HANDLE:
    try:
        return GetStdHandle(STD_OUTPUT_HANDLE)
    except ctypes.WinError as exc:
        raise OSError("Unable to obtain stdout handle.") from exc

def _get_console_mode(handle: wintypes.HANDLE) -> wintypes.DWORD:
    mode = wintypes.DWORD()
    try:
        GetConsoleMode(handle, ctypes.byref(mode))
    except ctypes.WinError as exc:
        raise OSError("Unable to obtain console mode.") from exc
    return mode

def _set_console_mode(handle: wintypes.HANDLE, mode: wintypes.DWORD):
    try:
        return SetConsoleMode(handle, mode)
    except ctypes.WinError as exc:
        raise OSError("Unable to set console mode.") from exc

def enable():
    handle = _get_stdout_handle()
    mode = _get_console_mode(handle)
    if mode.value & ENABLE_VIRTUAL_TERMINAL != ENABLE_VIRTUAL_TERMINAL:
        mode.value |= ENABLE_VIRTUAL_TERMINAL
        _set_console_mode(handle, mode)

def disable():
    handle = _get_stdout_handle()
    mode = _get_console_mode(handle)
    if mode.value & ENABLE_VIRTUAL_TERMINAL != 0:
        mode.value &= ~ENABLE_VIRTUAL_TERMINAL
        _set_console_mode(handle, mode)

def is_enabled():
    handle = _get_stdout_handle()
    mode = _get_console_mode(handle)
    return mode.value & ENABLE_VIRTUAL_TERMINAL == ENABLE_VIRTUAL_TERMINAL

