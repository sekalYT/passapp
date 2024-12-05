import sqlite3
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

from config.config import locale
from locales.languages import *

script_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_dir, '..', 'data.db')
database_path = os.path.abspath(database_path)

class Extract:
    def __init__(self, master_key):
        self.master_key = master_key
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        cur.execute('SELECT id, service, login, password, salt FROM loginsdata')
        self.records = cur.fetchall()
        self.print_records()
        conn.close()

    def generate_key(self, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.master_key.encode()))
        return key

    def decrypt_password(self, encrypted_password, salt):
        try:
            key = self.generate_key(salt)
            f = Fernet(key)
            decrypted_password = f.decrypt(encrypted_password.encode()).decode()
            return decrypted_password
        except Exception as e:
            print(f"{Languages[locale['Choice']]['Decrypterror']}: {e}")
            return "Decryption failed"

    def print_records(self):
        for record in self.records:
            id, service, login, encrypted_password, salt = record
            decrypted_password = self.decrypt_password(encrypted_password, salt)
            print(f"ID: {id}, {Languages[locale['Choice']]['Service']}: {service}, {Languages[locale['Choice']]['Login']}: {login}, {Languages[locale['Choice']]['Password']}: {decrypted_password}")