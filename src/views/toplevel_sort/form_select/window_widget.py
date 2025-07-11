import tkinter as tk
import hook.screen as hook
from .window_event import send_table
from .window_constant import radio_config
from views.window_constant import other
from views.window_constant import color
from views.window_constant import typography

def form(data):
    root = tk.Toplevel() 
    size_screen = hook.screen_config(root, 125, 130)

    root.geometry(f'250x260+{size_screen['width_offset']}+{size_screen['height_offset']}')
    root.iconbitmap(other['icon'])
    root.title('Форма выбора сортировки')
    root.configure(bg = color['cobalt'])
    root.resizable(False, False)

    label = tk.Label(
        root,
        text = 'Сортировать по:',
        anchor = 'w',
        font = typography['arial_10_i'],
        bg = color['cobalt'],
        fg = color['white'],
        padx = 10,
    )
    label.pack(
        anchor = 'w',
        pady = 5
    )


    selected = tk.StringVar(root) 
    selected.set(None)

    for (value, text) in radio_config.items():
        radiobutton = tk.Radiobutton(
            root,
            text = text, 
            value = value,
            variable = selected,
            width = 16,
            anchor = 'w',
            font = typography['arial_10_i'],
            bg = color['cobalt'],
            activebackground = color['cobalt'],
            fg = color['white'],
            activeforeground = color['white'],
            cursor = 'hand2',
            selectcolor = color['cobalt'],
            command = lambda sort = value, data = data: send_table(root, sort, data)
        )
        radiobutton.pack(
            side = 'top', 
            anchor = 'center',
            ipady = 5
        )
 
    root.grab_set()
    root.mainloop() 