import re
def null_string(value):
    if len(value) > 0:
        status =  True
    else:
        status = False
    return status

def length_string(value, symbol):
    if symbol[0] < len(value) <= symbol[1]:
        status =  True
    else:
        status = False
    return status

def email(value):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, value) or value == '':  
        return True  
    else:  
        return False  
    
def tel(value):
    pattern = r'^8\d{10}$'
    if re.match(pattern, value):  
        return True  
    else:  
        return False  