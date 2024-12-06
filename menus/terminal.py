from base_interface import BaseInterface
from functionsapp.reg import Registration
from functionsapp.extract import Extract
from functionsapp.delete import Remover
from functionsapp.generator import Generatorpass
from functionsapp.upload_download import FileSync
from config.config import locale, settings, save_settings, settings_path
from locales.languages import *

import os
import uuid
from config.config import locale, settings, save_settings, settings_path
from locales.languages import Languages
from functionsapp.upload_download import FileSync

class Terminal(BaseInterface):
    @classmethod 
    def run(cls):
        file_sync = cls._get_file_sync_instance()
        while True:
            print('-------------------------------------------------------')
            print(Languages[locale['Choice']]['Menu'] + "\n7 - Upload data.db\n8 - Download data.db")
            try:
                choice = int(input())
                if choice == 1:
                    cls.TerminalRegistration()
                elif choice == 2:
                    cls.TerminalExtract()
                elif choice == 3:
                    cls.TerminalRemover()
                elif choice == 4:
                    cls.TerminalGenerator()
                elif choice == 5:
                    print(Languages[locale['Choice']]['Inputlang'])
                    newlang = input()
                    newlang = newlang.upper()
                    locale['Choice'] = f'{newlang}'
                    settings['language'] = locale['Choice']
                    save_settings(settings_path, settings)
                
                elif choice == 6:
                    print(Languages[locale['Choice']]['Exit'])
                    break
                
                elif choice == 7:
                    file_sync.upload_file()
                
                elif choice == 8:
                    file_sync.download_file()
                
                else:
                    print(Languages[locale['Choice']]['Invalidinput'])
            
            except ValueError:
                print(Languages[locale['Choice']]['Invalidinput'])

    @classmethod
    def _get_file_sync_instance(cls):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(current_dir))
        config_dir = os.path.join(project_root, 'passapp', 'config')
        
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)
        
        id_file_path = os.path.join(config_dir, 'id.txt')

        if not os.path.exists(id_file_path):
            user_id = str(uuid.uuid4())
            with open(id_file_path, 'w') as id_file:
                id_file.write(user_id)
            print(f"Generated new user ID: {user_id}")
        else:
            with open(id_file_path, 'r') as id_file:
                user_id = id_file.read().strip()
            print(f"Read existing user ID: {user_id}")
        
        save_settings(settings_path, settings)

        return FileSync('http://94.241.171.222:8080', user_id)



    @classmethod
    def TerminalRegistration(cls):
        print("Enter master key for encryption:")
        master_key = input()
        print(Languages[locale['Choice']]['Servicename'])
        inputservice = input()
        print(Languages[locale['Choice']]['Logininput'])
        inputlogin = input()
        print(Languages[locale['Choice']]['Passwordinput'])
        inputpassword = input()
        print(Languages[locale['Choice']]['Resultdata'])
        Registration(inputservice, inputlogin, inputpassword, master_key)
    
    @classmethod
    def TerminalRemover(cls):
        deleteid = input(Languages[locale['Choice']]['Idremove'])
        if deleteid.isdigit():
            Remover(deleteid)
        else:
            print(Languages[locale['Choice']]['Invalidinput'])

    @classmethod
    def TerminalExtract(cls):
        print("Enter master key for decryption:")
        master_key = input()
        Extract(master_key)

    @classmethod
    def TerminalGenerator(cls):
        print(Languages[locale['Choice']]['Lenghtpass'])
        try:
            lenght = int(input())
            print(Languages[locale['Choice']]['Specifysymbols'])
            choicespecific = input()
            
            if choicespecific not in ['Y', 'y', 'N', 'n']:
                print(Languages[locale['Choice']]['Invalidinput'])
                return
            
            Generatorpass(lenght, choicespecific)
        
        except ValueError:
            print(Languages[locale['Choice']]['Invalidinput'])