import tkinter as tk
import hook.screen as hook
from .table_constant import table_config
from views.window_constant import color
from views.window_constant import typography
from .table_event import editing
from .table_event import handle_click
from .table_event import on_enter
from .table_event import on_leave

def table(master, data):
    labels = []
    size_screen = hook.screen_config(master, 225, 225)

    frame_title = tk.Frame(
        master, 
        width = size_screen['width_return'] * 0.88,
        height = 46,
        relief = 'raised',
        borderwidth = 1
    )
    frame_title.grid()
    frame_title.grid_propagate(False)

    for i, el in enumerate(table_config['heading']):
        label = tk.Label(
            frame_title, 
            text = el, 
            anchor = 'center',
            font = typography['helvetica_12_i'],
            bg = color['light_grey'],
            fg = color['smoky_white']
        )
        label.place(
            relx = 0.25 * i,
            relwidth = 0.25,
            height = 44
        )

#-------------------------
    frame_content = tk.Frame(
        master,
        width = size_screen['width_return'] * 0.88
    )
    frame_content.grid(
        sticky = 'nsew'
    )
    frame_content.grid_propagate(False)
    master.grid_rowconfigure(frame_content, weight = 1)

    canvas = tk.Canvas(
        frame_content, 
        bg = color['white']
    )
    scrollbar = tk.Scrollbar(
        frame_content, 
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
        bg = color['white']
    )
    frame.pack()

    canvas.create_window(
        (0, 0), 
        window = frame,
        anchor = 'nw'
    )

#-------------------------
    for i, el in enumerate(data):
 
        name = el[1]
        patronymic = el[2]
        surname = el[3]
        firm = el[4]
        post = el[5]
        phone = el[6]
        mail = el[7]

        t = str(phone)
        tel = f'{t[0:1]} – ({t[1:4]}) – {t[4:6]} – {t[6:8]} – {t[8:11]}'
        row = [editing(name, patronymic, surname), editing(post, ' ', firm), tel, mail]
        current_data = data[i]
        i = tk.Frame(
            frame, 
            width = size_screen['width_return'] * 0.88 - 16, 
            height = 46,
            relief = 'raised',
            borderwidth = 1,
        )
        i.grid()
        i.grid_propagate(0)
    
        row_labels = []
        for j, el_item in enumerate(row):
            
            label = tk.Label(
                i, 
                text = el_item, 
                anchor = 'w',
                font = typography['arial_10_i'],
                bg = color['white'],
                fg = color['cobalt'],
                padx = 10,
                justify = 'left',
                cursor = 'hand2'
            )
            label.place(
                relx = 0.25 * j,
                relwidth = 0.25,
                height = 44
            )
            label.bind(
                '<Button-1>', 
                lambda label, send_data = current_data, widget = master: handle_click(send_data, widget)
            )

            label.bind(
                '<Enter>', 
                lambda label, key = i: on_enter(key)
            )

            label.bind(
                '<Leave>', 
                lambda label, key = i: on_leave(key)
            )
            row_labels.append(label)
        labels.append(row_labels)

    
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