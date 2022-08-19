import enum as _enum

ESCAPE_SEQUENCE = '\x1b['

def cursor_up(n=1, /):
    return ESCAPE_SEQUENCE + str(n) + 'A'

def cursor_down(n=1, /):
    return ESCAPE_SEQUENCE + str(n) + 'B'

def cursor_forward(n=1, /):
    return ESCAPE_SEQUENCE + str(n) + 'C'

def cursor_backward(n=1, /):
    return ESCAPE_SEQUENCE + str(n) + 'D'

def cursor_next_line(n=1, /):
    return ESCAPE_SEQUENCE + str(n) + 'E'

def cursor_previous_line(n=1, /):
    return ESCAPE_SEQUENCE + str(n) + 'F'

def cursor_horizontal_absolute(x):
    return ESCAPE_SEQUENCE + str(x) + 'G'

def cursor_vertical_absolute(y):
    return ESCAPE_SEQUENCE + str(y) + 'd'

def cursor_save():
    return ESCAPE_SEQUENCE + 's'

def cursor_restore():
    return ESCAPE_SEQUENCE + 'u'

def cursor_position(x, y):
    return ESCAPE_SEQUENCE + str(y) + ';' + str(x) + 'H'

cursor_position_absolute = cursor_position

def cursor_position_relative(x, y):
    return ESCAPE_SEQUENCE + str(y) + ';' + str(x) + 'f'

def cursor_enable_blink():
    return ESCAPE_SEQUENCE + '?12h'

def cursor_disable_blink():
    return ESCAPE_SEQUENCE + '?12l'

def cursor_show():
    return ESCAPE_SEQUENCE + '?25h'

def cursor_hide():
    return ESCAPE_SEQUENCE + '?25l'

class CursorShapes(_enum.Enum):
    DEFAULT = 0
    BLINKING_BLOCK = 1
    STEADY_BLOCK = 2
    BLINKING_UNDERLINE = 3
    STEADY_UNDERLINE = 4
    BLINKING_BAR = 5
    STEADY_BAR = 6

def cursor_shape(shape: CursorShapes):
    return ESCAPE_SEQUENCE + str(shape.value) + " q"

def scroll_up(n=1, /):
    """Scroll the viewport up n lines"""
    return ESCAPE_SEQUENCE + str(n) + 'T'

def scroll_down(n=1, /):
    """Scroll the viewport down n lines"""
    return ESCAPE_SEQUENCE + str(n) + 'S'

def insert_character(n=1, /):
    return ESCAPE_SEQUENCE + str(n) + '@'

insert_space = insert_character

def delete_character(n=1, /):
    return ESCAPE_SEQUENCE + str(n) + 'P'

def erase_character(n=1, /):
    return ESCAPE_SEQUENCE + str(n) + 'X'

def insert_line(n=1, /):
    return ESCAPE_SEQUENCE + str(n) + 'L'

def delete_line(n=1, /):
    return ESCAPE_SEQUENCE + str(n) + 'M'

class EraseModes(_enum.Enum):
    CURSOR_TO_END = 0
    BEGINNING_TO_CURSOR = 1
    ALL = 2

def erase_line(mode=EraseModes.CURSOR_TO_END):
    return ESCAPE_SEQUENCE + str(mode.value) + 'K'

def erase_display(mode=EraseModes.ALL):
    return ESCAPE_SEQUENCE + str(mode.value) + 'J'

class TextFormats(_enum.Enum):
    DEFAULT = 0
    
    BOLD = 1
    NO_BOLD = 22

    UNDERLINE = 4
    NO_UNDERLINE = 24

    NEGATIVE = 7
    NO_NEGATIVE = 27
    POSITIVE = 27

    FOREGROUND_BLACK = 30
    FOREGROUND_RED = 31
    FOREGROUND_GREEN = 32
    FOREGROUND_YELLOW = 33
    FOREGROUND_BLUE = 34
    FOREGROUND_MAGENTA = 35
    FOREGROUND_CYAN = 36
    FOREGROUND_WHITE = 37
    BRIGHT_FOREGROUND_BLACK = 90
    BRIGHT_FOREGROUND_RED = 91
    BRIGHT_FOREGROUND_GREEN = 92
    BRIGHT_FOREGROUND_YELLOW = 93
    BRIGHT_FOREGROUND_BLUE = 94
    BRIGHT_FOREGROUND_MAGENTA = 95
    BRIGHT_FOREGROUND_CYAN = 96
    BRIGHT_FOREGROUND_WHITE = 97
    FOREGROUND_DEFAULT = 39

    BACKGROUND_BLACK = 40
    BACKGROUND_RED = 41
    BACKGROUND_GREEN = 42
    BACKGROUND_YELLOW = 43
    BACKGROUND_BLUE = 44
    BACKGROUND_MAGENTA = 45
    BACKGROUND_CYAN = 46
    BACKGROUND_WHITE = 47
    BRIGHT_BACKGROUND_BLACK = 100
    BRIGHT_BACKGROUND_RED = 101
    BRIGHT_BACKGROUND_GREEN = 102
    BRIGHT_BACKGROUND_YELLOW = 103
    BRIGHT_BACKGROUND_BLUE = 104
    BRIGHT_BACKGROUND_MAGENTA = 105
    BRIGHT_BACKGROUND_CYAN = 106
    BRIGHT_BACKGROUND_WHITE = 107
    BACKGROUND_DEFAULT = 49

def format_text(*formats: TextFormats):
    """Format the viewport text according to the given formats
    
    Note:
        The order of the formats matters.
        We do not support extended formats.
    """
    if not formats:
        formats = (TextFormats.DEFAULT,)
    elif len(formats) > 16:
        raise ValueError("Too many formats")
    return (ESCAPE_SEQUENCE +
        ";".join([str(format.value) for format in formats]) +
        'm')

def set_title(title):
    return '\x1b]0;' + title + '\x1b\x5c'

def alternate_screen_buffer():
    return ESCAPE_SEQUENCE + '?1049h'

def main_screen_buffer():
    return ESCAPE_SEQUENCE + '?1049l'
