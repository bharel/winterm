import ctypes
from ctypes import wintypes

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
GetStdHandle.argtypes = [ctypes.c_int]
GetStdHandle.restype = ctypes.c_void_p
GetStdHandle.errcheck = errcheck

def enable():
    pass

def disable():
    pass

def is_enabled():
    pass

