from tkinter import messagebox
from .window_constant import window_config
import views.toplevel_user.form_send.main as main
from views.frame_bottom.main import update_table

def handler_click(root, data):
    if data['requests'] == 'update':
        root.destroy()
        window_config[data['requests']]['requests'](data)
    elif data['requests'] == 'delete':
        if data['id_party'] == 1:
            messagebox.showinfo(
                title = window_config[data['requests']]['title'],
                message = 'Установлен запрет\nна удаление группы'
            )
        else:
            error = window_config[data['requests']]['requests']('party', {'id_party' : data['id_party']})
            if not error:
                messagebox.showinfo(
                    title = window_config[data['requests']]['title'],
                    message = 'Группа контактов - удалена'
                )
            else:
                messagebox.showerror(
                    title = window_config[data['requests']]['title'],
                    message = 'Группа контактов не удалена\n' \
                              'повторите попытку позже'     
                )  
            root.destroy()
    elif data['requests'] == 'get':
        root.destroy()
        main.get_data(data)
#-------------------------------
    elif data['requests'] == 'group_contacts':
        root.destroy()
        widget = data['widget']
        id = {'id_party' : data['id_party']}
        update_table(widget, id)
#-------------------------------
    else:
        root.destroy()
        window_config[data['requests']]['requests'](data)