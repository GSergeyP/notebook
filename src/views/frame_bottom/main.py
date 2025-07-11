from api import read_data
from tkinter import messagebox
from .table_widget import table
from views.frame_top.buttons_constant import variable

def update_table(widget, id = False, column = False, order_sort = False):
    variable[0] = id
    for child in widget.winfo_children():
        child.destroy()
    frame_bottom(widget, id, column, order_sort)

def frame_bottom(master, id = False, column = False, order_sort = False): 
    data, error = read_data(
        'users', 
        [
            'id_users', 
            'name', 
            'patronymic', 
            'surname', 
            'firm', 
            'post',
            'phone',
            'mail',
            'id_party'
        ], 
        id,
        column,
        order_sort
        )
    if error:
        messagebox.showinfo(
            title = 'Контакты',
            message = 'Контакты не доступны\n' \
                      'повторите попытку позже'
            )
    else:
        table(master, data)