from base_interface import BaseInterface
from functionsapp.reg import Registration
from functionsapp.extract import Extract
from functionsapp.delete import Remover
from functionsapp.generator import Generatorpass
from config.config import locale, settings, save_settings, settings_path
from locales.languages import *

class Terminal(BaseInterface):
    @classmethod 
    def run(cls):
        while True:
            print('-------------------------------------------------------')
            print(Languages[locale['Choice']]['Menu'])
            choice = int(input())
            if choice == 1:
                cls.TerminalRegistration()
            elif choice == 2:
                Extract()
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

    @classmethod
    def TerminalRegistration(cls):
        print(Languages[locale['Choice']]['Servicename'])
        inputservice = input()
        print(Languages[locale['Choice']]['Logininput'])
        inputlogin = input()
        print(Languages[locale['Choice']]['Passwordinput'])
        inputpassword = input()
        print(Languages[locale['Choice']]['Resultdata'])
        Registration(inputservice, inputlogin, inputpassword)
    
    @classmethod
    def TerminalRemover(cls):
        deleteid = input()
        if deleteid.isdigit():
            Remover(deleteid)
        else:
            print(Languages[locale['Choice']]['Invalidinput'])

    @classmethod
    def TerminalGenerator(cls):
        print(Languages[locale['Choice']]['Lenghtpass'])
        lenght = int(input())
        print(Languages[locale['Choice']]['Specifysymbols'])
        try:
            choicespecific = input()
        except choicespecific not in ['Y', 'y', 'N', 'n']:
            print(Languages[locale['Choice']]['Invalidinput'])
        Generatorpass(lenght, choicespecific)