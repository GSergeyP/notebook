import views.toplevel_user.widget_choose as form
from views.window_constant import color


def editing(t1, t2 = False, t3 = False):
    if all([t1, t2, t3]):
        msg = t3 + '\n' + t1 + ' ' + t2
    elif all([t1, t2]):
        msg = t1 + ' ' + t2
    elif all([t1, t3]):
        msg = t3 + ' ' + t1
    elif all([t3, t2]):
        msg = t3 + ' ' + t2
    else:
        msg = t1
    return msg

def on_enter(event):
    for el in event.winfo_children():
        el.config(bg = color['smoky_white'])

def on_leave(event):
    for el in event.winfo_children():
        el.config(bg = color['white'])
     
def handle_click(data, widget):
    form.toplevel_user({'requests' : 'update', 'data' : data, 'widget' : widget})