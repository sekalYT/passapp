import sqlite3
import os
import random
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import requests

script_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_dir, '..', 'data.db')
database_path = os.path.abspath(database_path)

class Registration:
    idslist = []

    def __init__(self, service, login, password, master_key):
        self.service = service
        self.login = login
        self.password = password
        self.master_key = master_key
        self.register()

    def generate_key(self, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.master_key.encode()))
        return key

    def encrypt_password(self, password, salt):
        key = self.generate_key(salt)
        f = Fernet(key)
        encrypted_password = f.encrypt(password.encode()).decode()
        return encrypted_password

    def register(self):
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        cur.execute("CREATE TABLE if NOT EXISTS loginsdata(id, service, login, password, salt)")
        
        id = self.ids()
        salt = os.urandom(16)
        encrypted_password = self.encrypt_password(self.password, salt)
        
        cur.execute('INSERT INTO loginsdata (id, service, login, password, salt) VALUES (?, ?, ?, ?, ?)', 
                    (id, self.service, self.login, encrypted_password, salt))
        conn.commit()
        conn.close()

    def ids(self):
        try:
            count = 1
            while count:
                id = random.randint(0, 99999999)
                if id in Registration.idslist:
                    continue
                else:
                    Registration.idslist.append(id)
                    break
            return id
        except:
            print('LOG: Unexpected Error')