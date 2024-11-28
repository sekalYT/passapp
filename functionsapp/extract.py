import sqlite3
import os
from config.config import locale
from locales.languages import *

script_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_dir, '..', 'data.db')
database_path = os.path.abspath(database_path)
conn = sqlite3.connect(database_path)

class Extract:
    def __init__(self):
        cur = conn.cursor()
        cur.execute('SELECT id, service, login, password FROM loginsdata')
        self.records = cur.fetchall()
        self.print_records()


    def print_records(self):
        for record in self.records:
            id, service, login, password = record
            print(f"ID: {id}, {Languages[locale['Choice']]['Service']}: {service}, {Languages[locale['Choice']]['Login']}: {login}, {Languages[locale['Choice']]['Password']}: {password}")
