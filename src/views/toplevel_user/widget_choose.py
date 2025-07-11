from .form_send.main import form_send
from views.toplevel_group.widget_choose import toplevel_group

def toplevel_user(widget):
    widget['party'] = False
    match widget['requests']:  
        case 'add': 
            form_send(widget)
        case 'update': 
            widget['party'] = True
            form_send(widget)
        case 'group_contacts':
            toplevel_group(widget)
        case _: 
            pass
