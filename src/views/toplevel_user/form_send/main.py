from api import read_data
from tkinter import messagebox
from .window_widget import form
from .window_constant import variables

def get_data(data):
    variables['id_party'] = data['id_party']
    variables['button'].config(text = data['name'])   

def get_label_button(data): 
    if data['party']:
        variables['id_party'] = data['data'][8]
        data_db, error = read_data('party', ['name'], {'id_party' : data['data'][8]})
        if error:
            messagebox.showinfo(
                title = 'Получение названия группы',
                message =   'Группа контактов не доступна\n' \
                            'повторите попытку позже'
                )
        else:
            variables['button'].config(text = data_db[0][0])

def form_send(data):
    form(data)
    get_label_button(data)