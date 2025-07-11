from tkinter import messagebox
from .window_constant import window_config
from hook.validate import null_string
from hook.validate import length_string

def handle_click(root, value, data):
    value = value.strip()
    if  not null_string(value) or \
        not length_string(value, [0, 20]):
        messagebox.showerror(
            title = window_config[data['requests']]['title'],
            message = 'Обязательное поле,\nНе более 20 символов'           
        )
    else:
        if data['requests'] == 'add':
            error = window_config[data['requests']]['requests']('party', {'name' : value})
        else:
            error = window_config[data['requests']]['requests']('party', {'name' : value}, {'id_party' : data['id_party']})
        if not error:
            messagebox.showinfo(
                title = window_config[data['requests']]['title'],
                message = 'Группа контактов - ' +  window_config[data['requests']]['message']    
            )
        else:
            messagebox.showerror(
                title = window_config[data['requests']]['title'],
                message = 'Группа контактов не' + \
                           window_config[data['requests']]['message'].lower() + ' \n' \
                          'повторите попытку позже'     
            )  
        root.destroy()