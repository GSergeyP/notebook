import tkinter as tk
import hook.screen as hook
from views.toplevel_group.form_send.window_event import handle_click
from .window_constant import window_config
from views.window_constant import other
from views.window_constant import color
from views.window_constant import typography

def form(data):
    root = tk.Toplevel() 
    size_screen = hook.screen_config(root, 125, 75)

    root.geometry(f'250x150+{size_screen['width_offset']}+{size_screen['height_offset']}')
    root.iconbitmap(other['icon'])
    root.title(window_config[data['requests']]['title'])
    root.configure(
        bg = color['cobalt']
    )
    root.resizable(False, False)

    label = tk.Label(
        root,
        text = window_config[data['requests']]['label_text'],
        bg = color['cobalt'],
        fg = color['white'],
        font = typography['arial_10_i']
    )
    label.place(
        relx = 0.05,
        rely = 0.1,
    )

    entry = tk.Entry(
        root, 
        font = typography['arial_12'],
        width = 23,
        bg = color['smoky_white'],
        relief = tk.RIDGE
    )
    entry.place(
        relx = 0.5, 
        rely = 0.38, 
        anchor = 'center',
        height = 25
    )
    if data['requests'] == 'update':
        entry.insert(0, data['name']) 

    button = tk.Button(
        root,
        text = window_config[data['requests']]['button_text'],
        font = typography['arial_10_i'],
        width = 25,
        bg = color['smoky_white'],
        fg = color['cobalt'],
        borderwidth = 0,
        cursor = 'hand2',
        command = lambda: handle_click(root, entry.get(), data)
    )
    button.place(
        relx = 0.5, 
        rely = 0.7, 
        anchor = 'center',
        height = 25
    )

    root.grab_set()