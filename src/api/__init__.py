get_connection = (
                    'src/db/contactlist.db'
                 )

__all__ = (
            'execute_query', 
            'execute_read_query',
            'insert_into',
            'read_data',
            'update',
            'delete'
          )

from .connect import execute_query
from .connect import execute_read_query
from .requests import insert_into
from .requests import read_data
from .requests import update
from .requests import delete