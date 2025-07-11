import tkinter as tk
import hook.screen as hook
from .window_event import handler_click
from .window_constant import window_config
from views.window_constant import other
from views.window_constant import color
from views.window_constant import typography

def form(data, data_db):
    root = tk.Toplevel() 
    size_screen = hook.screen_config(root, 125, 75)
    root.geometry(f'250x150+{size_screen['width_offset']}+{size_screen['height_offset']}')
    root.iconbitmap(other['icon'])
    root.title(window_config[data['requests']]['title'])
    root.resizable(False, False)
    
    canvas = tk.Canvas(
        root, 
        bg = color['cobalt']
    )
    scrollbar = tk.Scrollbar(
        root, 
        orient = 'vertical', 
        command = canvas.yview
    )
    scrollbar.pack(
        side = 'right', 
        fill = 'y',
    )
    canvas.config(
        yscrollcommand = scrollbar.set,
        highlightthickness = 0
    )
    canvas.pack(
        side = 'left', 
        fill = 'both', 
        expand = True
    )
    frame = tk.Frame(
        canvas,
        bg = color['cobalt'],

    )
    canvas.create_window(
        (0, 0), 
        window = frame, 
        anchor = 'nw', 
        tags = ('frame')
    )
    
    for el in data_db:
        tk.Button(
            frame, 
            text = el[1], 
            width = 25, 
            font = typography['arial_10_i'],
            bg = color['cobalt'],
            fg = color['smoky_white'],
            activebackground = color['cobalt'],
            activeforeground = color['smoky_white'],
            borderwidth = 0,
            cursor = 'hand2',
            anchor = 'w',
            command = lambda el = el: handler_click(root, data | {'id_party' : el[0], 'name' : el[1]})
        ).pack(
            padx = 10,
            anchor = 'center',
            pady = 2
        )
        
    def _bound_to_mousewheel(event):
        frame.bind_all('<MouseWheel>', _on_mousewheel)

    def _unbound_to_mousewheel(event):
        frame.unbind('<MouseWheel>')

    def _on_mousewheel(event):
        if frame.winfo_height() <= canvas.winfo_height():
            factor = 0
        else:
            factor = 1

        canvas.yview_scroll(factor * int(-1 * (event.delta / 120)), 'units')

    frame.bind(
        '<Configure>', 
        lambda e: canvas.config(scrollregion = canvas.bbox('all'))
    )
    frame.bind('<Enter>', _bound_to_mousewheel)
    frame.bind('<Leave>', _unbound_to_mousewheel)

    root.grab_set()