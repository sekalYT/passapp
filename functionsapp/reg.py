import sqlite3
import os
import random

script_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_dir, '..', 'data.db')
database_path = os.path.abspath(database_path)


class Registration:
    def __init__(self, service, login, password):
        self.service = service
        self.login = login
        self.password = password
        self.register()

    def register(self):
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        cur.execute("CREATE TABLE if NOT EXISTS loginsdata(id, service, login, password)")
        id = random.randint(0, 9999999)
        cur.execute('INSERT INTO loginsdata (id, service, login, password) VALUES (?, ?, ?, ?)', (id, self.service, self.login, self.password))
        conn.commit()
        conn.close()
    
