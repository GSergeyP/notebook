import tkinter as tk
from views.window_constant import color

def logo(master):
    image = tk.PhotoImage(file = 'src/assets/logo.png')
    label = tk.Label(
        master,
        width = 154,
        height = 100,
        image = image,
        bg = color['cobalt'],
        anchor = 'center'
    )
    label.image = image
    label.grid(
        pady = 3
    )