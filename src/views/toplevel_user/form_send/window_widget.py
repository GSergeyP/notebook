import tkinter as tk
import hook.screen as hook
import views.toplevel_user.form_send.window_constant as constant
from .window_constant import frame_config
from .window_constant import requests
from .window_constant import variables
from views.window_constant import other
from views.window_constant import color
from views.window_constant import typography

def form(data):
    button_config = requests(data)
    variables['requests'] = data['requests']
    variables['widget'] = data['widget']

    
    if variables['requests'] == 'add':
        variables['id_party'] = 1
    if data.get('data', False):
        variables['id_users'] = data['data'][0]


    root = tk.Toplevel() 
    variables['root'] = root
    size_screen = hook.screen_config(root, 200, 200)


    root.geometry(f'400x400+{size_screen['width_offset']}+{size_screen['height_offset']}')
    root.iconbitmap(other['icon'])
    root.title(constant.window_config[data['requests']]['title'])
    root.configure(bg = color['cobalt'])
    root.resizable(False, False)

#-------------------------  
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
        bg = color['cobalt']
    )

    canvas.create_window(
        (0, 0), 
        window = frame, 
        anchor = 'nw', 
        tags = ('frame')
    )

#-------------------------  
    label = tk.Label(
        frame,
        text = 'Поля, помеченные знаком звёздочки (*),\nобязательные для заполнения.',
        bg = color['cobalt'],
        fg = color['white'],
        font = typography['arial_10_i']
    )
    label.pack(
        anchor = 'center',
        pady = 1
    )
#  
    for i, el in enumerate(frame_config):
        tk.Label(
            frame,
            width = 45,
            text = el['label'],
            bg = color['cobalt'],
            fg = color['white'],
            font = typography['arial_10_i'],
            anchor = 'sw',
            height = 2
        ).pack(
            anchor = 'center',
            pady = 1,
            side = el['side']

        )
        variables[el['entry']] = tk.Entry(
            frame,
            width = 40,
            font = typography['arial_12'],
            bg = color['smoky_white'],
            relief = tk.RIDGE,
        )
        variables[el['entry']].pack(
            anchor = 'center',
            pady = 2,
            side = el['side']
        )
        if data['requests'] == 'update' and data['data'][i + 1]:
            variables[el['entry']].insert(0, data['data'][i + 1])
    
    for el in button_config:
        if el['label']:
            tk.Label(
                frame,
                width = 45,
                text = el['label'],
                bg = color['cobalt'],
                fg = color['white'],
                font = typography['arial_10_i'],
                anchor = 'sw',
                height = 2
            ).pack(
                anchor = 'center',
                pady = 1,
                side = el['side']
            )
        button = tk.Button(
            frame,
            text = el['text'],
            font = typography['arial_10_i'],
            width = el['width'],
            bg = color['smoky_white'],
            fg = color['cobalt'],
            borderwidth = 0,
            cursor = 'hand2',
            command = el['event'],
            anchor = el['anchor_text']
        )
        button.pack(
            anchor = el['anchor'],
            pady = el['pady'],
            padx = [10, 10],
            side = el['side']
        )
        if el['label']:
            variables['button'] = button


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