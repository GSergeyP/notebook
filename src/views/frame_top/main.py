from .buttons_widget import buttons
from .buttons_constant import variable

def get_party():
    return variable[0]

def frame_top(master, other_widget):
    buttons(master, other_widget)