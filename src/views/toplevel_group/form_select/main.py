from tkinter import messagebox
from api import read_data
from .window_constant import window_config
from .window_widget import form

def form_select(data):
    data_db, error = read_data('party', ['id_party', 'name'])

    if error:
        messagebox.showinfo(
            title = window_config[data['requests']]['title'],
            message = 'Группа контактов не доступна\n' \
                      'повторите попытку позже'
        )
    else:
        form(data, data_db)
