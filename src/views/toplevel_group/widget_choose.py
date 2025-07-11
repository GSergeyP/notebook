from .form_select.main import form_select
from .form_send.main import form_send

def toplevel_group(widget):
    match widget['requests']:  
        case 'add': 
            form_send(widget)
        case 'update': 
            form_select(widget)
        case 'delete':
            form_select(widget)
        case 'get':
            form_select(widget)
        case 'group_contacts':
            form_select(widget)
        case _: 
            pass
