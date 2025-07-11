from tkinter import messagebox
import views.frame_bottom.main as main
import views.toplevel_user.form_send.window_constant as constant
from hook.validate import null_string
from hook.validate import length_string
from hook.validate import email
from hook.validate import tel

def delete_db():
    constant.variables['requests'] = 'delete'

    error = constant.window_config[constant.variables['requests']]['requests'](
                'users', 
                {'id_users' : constant.variables['id_users']}
            )
    if not error:
        messagebox.showinfo(
            title = constant.window_config[constant.variables['requests']]['title'],
            message = 'Контакт удален \n' +  constant.window_config[constant.variables['requests']]['message']    
        )
    else:
        messagebox.showerror(
            title = constant.window_config[constant.variables['requests']]['title'],
            message = 'Контакт не удален\n' \
                      'повторите попытку позже'     
        ) 
    constant.variables['root'].destroy()
    main.update_table(constant.variables['widget'])



def add_update_db():
    name = constant.variables['name'].get().strip()
    patronymic = constant.variables['patronymic'].get().strip()
    surname = constant.variables['surname'].get().strip()
    firm = constant.variables['firm'].get().strip()
    post = constant.variables['post'].get().strip()
    phone = constant.variables['phone'].get().strip()
    mail = constant.variables['mail'].get().strip()

    try:
        constant.variables['id_party'] 
    except:
        constant.variables['id_party'] = 1
    id_party = constant.variables['id_party']

    error = {
        'name' : [all([null_string(name), length_string(name, [0, 20])]), 
                  'Имя - обязательное поле,\nНе более 20 символов'
                  ],
        'patronymic' : [length_string(patronymic, [-1, 20]),
                        'Отчество - не более 20 символов'
                        ],
        'surname' : [length_string(surname, [-1, 20]), 
                     'Фамилия - не более 20 символов'
                    ],

        'firm' : [length_string(firm, [-1, 50]),
                  'Организация - не более 50 символов'],
        'post' : [length_string(post, [-1, 30]),
                  'Должность - не более 30 символов'],
        'phone' : [tel(phone),
                  'Неправильный формат,\nПример: 8XXXXXXXXXX'],
        'mail' : [all([email(mail), length_string(mail, [-1, 20])]),
                  'Неправильный формат email,\nНе более 20 символов']
    }



    if not all([
        error['name'][0], \
        error['surname'][0], \
        error['patronymic'][0], \
        error['firm'][0], \
        error['post'][0], \
        error['phone'][0], \
        error['mail'][0]
    ]):
        msg = ''
        for el in [el for el in error if not error[el][0]]:
            msg += error[el][1] + '\n'
        messagebox.showerror(
            title = constant.window_config[constant.variables['requests']]['title'],
            message = msg       
    )
    else:
        data = {
            'name' : name,
            'patronymic' : patronymic,
            'surname' : surname,
            'firm' : firm,
            'post'  : post,
            'phone' : phone,
            'mail' : mail,
            'id_party' : id_party
        }

        if constant.variables['requests'] == 'add':
            error = constant.window_config[constant.variables['requests']]['requests']('users', data)
        else:
            error = constant.window_config[constant.variables['requests']]['requests'](
                'users', 
                data, 
                {'id_users' : constant.variables['id_users']}
            )
 
        if not error:
            messagebox.showinfo(
                title = constant.window_config[constant.variables['requests']]['title'],
                message = 'Контакт - ' +  constant.window_config[constant.variables['requests']]['message']    
            )
        else:
            messagebox.showerror(
                title = constant.window_config[constant.variables['requests']]['title'],
                message = 'Контакт не ' + \
                           constant.window_config[constant.variables['requests']]['message'].lower() + ' \n' \
                          'повторите попытку позже'     
            ) 
        constant.variables['root'].destroy()
        main.update_table(constant.variables['widget'])