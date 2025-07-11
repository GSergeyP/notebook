from .form_select.main import form_send

def toplevel_sort(widget):
    match widget['sort']:  
        case 'sort': 
            form_send(widget)
        case _: 
            pass
