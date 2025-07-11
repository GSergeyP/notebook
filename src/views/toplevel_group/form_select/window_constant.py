from views.toplevel_group.form_send.main import form_send
from api import delete

window_config = {
    'update' : {
        'title' : 'Изменение названия группы',
        'requests' : form_send
    },
    'delete' : {
        'title' : 'Удаление группы',
        'requests' : delete
    },
    'get' : {
        'title' : 'Список групп',
        'requests' : form_send
    },
    'group_contacts' : {
        'title' : 'Список групп',
        'requests' : form_send
    }
}
