import sqlite3

def create_connection(path):
    connection = None
    error = False
    try:
        connection = sqlite3.connect(path)
    except sqlite3.Error as e:
        #Вставить функцию для записи ошибки e
        error = True

    return connection, error


def execute_query(get_connection, query, value):
    connection, error = create_connection(get_connection)
    if not error:
        cursor = connection.cursor()
        try:
            cursor.execute('PRAGMA foreign_keys = ON')
            if value:
                cursor.execute(query, value)
            else:
                cursor.execute(query)
            connection.commit()
        except sqlite3.Error as e:
            #Вставить функцию для записи ошибки e
            error = True
        finally:
            cursor.close()
            connection.close()
    
    return error

def execute_read_query(get_connection, query, value):
    connection, error = create_connection(get_connection)
    result = None
    if not error:
        cursor = connection.cursor()
        try:
            if value:
                cursor.execute(query, value)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
        except sqlite3.Error as e:
            #Вставить функцию для записи ошибки e
            error = True
        finally:
            cursor.close()
            connection.close()

    return result, error