import views.toplevel_group.widget_choose as get_group
import views.toplevel_user.form_send.window_event as window
from api import insert_into
from api import update
from api import delete

variables = {}

frame_config = (
    {
        'label' : 'Имя*',
        'entry' : 'name',
        'side' : None
    },
    {
        'label' : 'Отчество',
        'entry' : 'patronymic',
        'side' : None
    },
    {
        'label' : 'Фамилия',
        'entry' : 'surname',
        'side' : None
    },
    {
        'label' : 'Организация',
        'entry' : 'firm',
        'side' : None
    },
    {
        'label' : 'Должность',
        'entry' : 'post',
        'side' : None
    },
    {
        'label' : 'Телефон*. Пример: 8XXXXXXXXXX',
        'entry' : 'phone',
        'side' : None
    },
    {
        'label' : 'Email',
        'entry' : 'mail',
        'side' : None
    }
    
)

window_config = {
    'add' : {
            'title' : 'Создание контакта',
            'message' : 'Создан',
            'requests' : insert_into
    },
    'update' : {
            'title' : 'Редактирование контакта',
            'message' : 'Изменен',
            'requests' : update
    },
    'delete' : {
            'title' : 'Удаление контакта',
            'message' : 'Изменения сохранены',
            'requests' : delete
    }
}

button_ofther = (
    {
        'label' : 'Текущая группа:',
        'text' : 'Общая',
        'event' : lambda: (get_group.toplevel_group({'requests' : 'get'})),
        'id' : 'btn_get_group',
        'width' : 44,
        'anchor_text' : 'w',
        'anchor' : 'center',
        'pady' : 1,
        'side' : None
    },

    {
        'label' : False,
        'text' : 'Сохранить',
        'event' : lambda: window.add_update_db(),
        'width' : 20,
        'anchor_text' : 'center',
        'anchor' : 'e',
        'pady' : 20,
        'side' : 'right'
    },
)

button_delete = (
    {
        'label' : False,
        'text' : 'Удалить',
        'event' : lambda: window.delete_db(),
        'width' : 21,
        'anchor_text' : 'center',
        'anchor' : 'w',
        'pady' : 20,
        'side' : 'right'
    },
    
)

def requests(requests):
    if requests['requests'] == 'update':
        button_config = button_ofther + button_delete
    else:
        button_config = button_ofther
    return button_config