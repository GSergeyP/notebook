import tkinter as tk
from views.toplevel_group.widget_choose import toplevel_group
from .buttons_constant import button_config
from views.window_constant import color
from views.window_constant import typography

def buttons(master):
    for el in button_config:
        image = tk.PhotoImage(file = el['src'])
        button = tk.Button(
            master, 
            width = 120, 
            height = 100,
            image = image,
            text = el['title'], 
            font = typography['arial_10_i'],
            fg = color['white'],
            activeforeground = color['white'],
            compound = 'top',
            bg = color['cobalt'],
            activebackground = color['cobalt'],
            borderwidth = 0,
            cursor = 'hand2',
            command = lambda el = el: toplevel_group({'requests' : el['event']})
        )
        button.image = image
        button.place(
            relx = 0.5, 
            y = el['y'], 
            anchor = 'center'
        )