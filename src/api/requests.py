from api import get_connection
from api import execute_query
from api import execute_read_query


def insert_into(table, data):
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data)
    placeholders = ', '.join(['?'] * len(data))
    values = tuple(el for el in (data.values()))
    sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % ( table, columns, placeholders )
    error = execute_query(get_connection, sql, values)

    return error


def read_data(table, data, id = False, column = False, order_sort = False):
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data)
    values = False
    if id:
        condition = ', '.join("{}=?".format(x) for x in id.keys())
        values = tuple(el for el in (id.values()))
        sql = "SELECT  %s  FROM %s  WHERE %s" % ( columns, table, condition)
    else:
        sql = "SELECT  %s  FROM %s" % (columns, table)

    if column:
        other = " ORDER BY %s %s" % (column, order_sort)
        sql += other

    return execute_read_query(get_connection, sql, values)


def update(table, data, id):
    columns = ', '.join("{}=?".format(x) for x in data.keys())
    condition = ', '.join("{}=?".format(x) for x in id.keys())
    values = tuple(el for x in (data.values(), id.values()) for el in x)
    sql = "UPDATE %s SET %s WHERE %s" % (table, columns, condition)
    error = execute_query(get_connection, sql, values)

    return error


def delete(table, id):
    columns = ', '.join("{}=?".format(x) for x in id.keys())
    values = tuple(el for el in (id.values()))
    sql = "DELETE FROM %s WHERE %s" % (table, columns)
    error = execute_query(get_connection, sql, values)

    return error 