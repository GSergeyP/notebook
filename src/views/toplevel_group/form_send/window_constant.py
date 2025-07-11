from api import insert_into
from api import update

window_config = {
    'add' : {
        'title' : 'Создание группы',
        'label_text' : 'Новая группа',
        'button_text' : 'Создать',
        'message' : 'Создана',
        'requests' : insert_into

    },
    'update' : {
        'title' : 'Изменение названия группы',
        'label_text' : 'Переименовать группу',
        'button_text' : 'Переименовать',
        'message' : 'Переименована',
        'requests' : update
    }
}