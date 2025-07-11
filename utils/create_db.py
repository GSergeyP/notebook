import os 
import sys
sys.path.append(os.getcwd() + '/src')
import api

create_party_table = """
                        CREATE TABLE IF NOT EXISTS party (
                            id_party INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(20) NOT NULL CHECK (LENGTH (name) <= 20)
                        );
                     """
create_users_table = """
                        CREATE TABLE IF NOT EXISTS users (
                            id_users INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(20) NOT NULL CHECK (LENGTH (name) <= 20),
                            patronymic VARCHAR(20) CHECK (LENGTH (patronymic) <= 20),
                            surname VARCHAR(20) CHECK (LENGTH (surname) <= 20),
                            firm VARCHAR(50) CHECK (LENGTH (firm) <= 50),
                            post VARCHAR(30) CHECK (LENGTH (post) <= 30),
                            phone INTEGER(11) NOT NULL CHECK (LENGTH (name) <= 11),
                            mail VARCHAR(20) NOT NULL CHECK (LENGTH (name) <= 20),
                            id_party INTEGER DEFAULT 1, 
                            FOREIGN KEY (id_party) REFERENCES party (id_party) ON DELETE SET DEFAULT
                        );"""

api.execute_query(api.get_connection, create_party_table, False)
api.execute_query(api.get_connection, create_users_table, False)
api.insert_into('party', {'name' : 'Общая'})