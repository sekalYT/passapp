import sqlite3
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_dir, '..', 'data.db')
database_path = os.path.abspath(database_path)

class Remover():
    def __init__(self, deleteid):
        self.deleteid = deleteid
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        print('Enter the ID for remove:')
        try:
            deletefunc = 'DELETE FROM loginsdata WHERE id = ?'
            cur.execute(deletefunc, (self.deleteid,))
            conn.commit()
        except:
            print('Invalid input or ID not found')
    