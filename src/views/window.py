import tkinter as tk
import hook.screen as hook
from views.window_constant import color
from views.window_constant import other
from .frame_top.main import frame_top as frame_top_widget
from .frame_left.main import frame_left as frame_left_widget
from .frame_bottom.main import frame_bottom as frame_bottom_widget
from views.toplevel_user.widget_choose import toplevel_user
from views.toplevel_group.widget_choose import toplevel_group
from views.toplevel_sort.widget_choose import toplevel_sort


def main():
    root = tk.Tk()
    size_screen = hook.screen_config(root, 225, 225)
    root.geometry(f'450x450+{size_screen['width_offset']}+{size_screen['height_offset']}')
    root.iconbitmap(other['icon'])
    root.title('Книга контактов — база данных')

#-------------------------
    frame_left = tk.Frame(
        root,
        width = 154,
        bg = color['cobalt']
    )
    frame_left.grid(
        row = 0, 
        column = 0, 
        rowspan = 2,
        sticky = 'nsew'
    )
    frame_left.grid_propagate(False)

#-------------------------
    frame_top = tk.Frame(
        root,
        height = 108,
        bg = color['smoky_white']
    ) 

    frame_top.grid(
        row = 0, 
        column = 1,
        sticky = 'nsew'
    )
    frame_top.grid_propagate(False)

#-------------------------
    frame_bottom = tk.Frame(
        root,
        bg = color['white']
    )
    frame_bottom.grid(
        row = 1, 
        column = 1,
        sticky = 'nsew'
    )
    frame_bottom.grid_propagate(False)

    root.grid_columnconfigure(frame_top, weight = 1)
    root.grid_rowconfigure(frame_bottom, weight = 1)
    root.grid_columnconfigure(frame_bottom, weight = 1)


    frame_top_widget(frame_top, frame_bottom)
    frame_left_widget(frame_left)
    frame_bottom_widget(frame_bottom)
    toplevel_user({'requests' : ''})
    toplevel_group({'requests' : ''})
    toplevel_sort({'sort' : ''})

    
    root.mainloop()