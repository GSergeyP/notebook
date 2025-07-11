import tkinter as tk
from views.toplevel_user.widget_choose import toplevel_user
from views.frame_bottom.main import update_table
from views.toplevel_sort.widget_choose import toplevel_sort
from .buttons_constant import button_config
from views.window_constant import color
from views.window_constant import typography
import views.frame_top.main as main


def buttons(master, other_widget):
    for el in button_config:
        if  el['event'] == 'common_contacts':
            event = lambda el = el: update_table(other_widget)
        elif el['event'] == 'sort':
            event = lambda el = el: toplevel_sort({'sort' : el['event'], 'widget' : other_widget, 'party' : main.get_party()})
        else:
            event = lambda el = el: toplevel_user({'requests' : el['event'], 'widget' : other_widget})

        image = tk.PhotoImage(file = el['src'])
        button = tk.Button(
            master, 
            width = 100, 
            height = 80,
            image = image,
            text = el['title'], 
            font = typography['arial_10_i'],
            fg = color['cobalt'],
            activeforeground = color['cobalt'],
            compound = 'top',
            bg = color['smoky_white'],
            activebackground = color['smoky_white'],
            borderwidth = 0,
            cursor = 'hand2',
            command = event
        )
        button.image = image
        button.place(
            x = el['x'], 
            rely = 0.5, 
            anchor = 'w'
        )