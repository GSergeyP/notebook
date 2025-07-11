def screen_config(widget, width, height):
    #Возврат количество пикселей экрана, на котором появляется окно
    width_return = widget.winfo_screenwidth() 
    height_return = widget.winfo_screenheight()
    #Cередина экрана
    width_middle = width_return // 2  
    height_middle = height_return // 2
    #Смещение от центра
    width_offset = width_middle - width
    height_offset = height_middle - height

    return {
        'width_offset' : width_offset,
        'height_offset' : height_offset,
        'width_return' : width_return,
        'height_return' : height_return
    }
