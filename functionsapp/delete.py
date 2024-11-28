import sqlite3
import os
from functionsapp.reg import Registration
from config.config import locale
from locales.languages import *

script_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_dir, '..', 'data.db')
database_path = os.path.abspath(database_path)

class Remover():
    def __init__(self, deleteid):
        self.deleteid = deleteid
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        try:
            deletefunc = 'DELETE FROM loginsdata WHERE id = ?'
            cur.execute(deletefunc, (int(self.deleteid),))
            if cur.rowcount == 0:
                print(Languages[locale['Choice']]['Idnotfound'])
            else:
                print(Languages[locale['Choice']]['Deleted'])
            conn.commit()
        except sqlite3.Error as e:
            print(Languages[locale['Choice']]['Invalidinput'])
            print(f"LOG: {e}")
        finally:
            conn.close()
    