from views.frame_bottom.main import update_table

def send_table(root, sort, data):
    id = data['party']
    widget = data['widget']
    column, order_sort = sort.split('_')
    update_table(widget, id, column, order_sort)
    root.after(100, lambda: root.destroy())
