from functionsapp.reg import Registration
from functionsapp.extract import Extract
from functionsapp.delete import Remover
from functionsapp.generator import Generatorpass


class Terminal:
    def menu1():
        while True:
            print('-------------------------------------------------------')
            print("""Choice the function:
1 - Register new account
2 - Extract from database
3 - Delete from database
4 - Generate new password
5 - Exit""")
            choice = int(input())
            if choice == 1:
                Terminal.TerminalRegistration()
            elif choice == 2:
                Extract()
            elif choice == 3:
                Terminal.TerminalRemover()
            elif choice == 4:
                Terminal.TerminalGenerator()
            elif choice == 5:
                print('Quiting...')
                break
    
    def TerminalRegistration():
        print('Enter the service name (Example: Amazon):')
        inputservice = input()
        print('Enter the login or email to this service (Example: iamvladislav@gmail.com or vlad333):')
        inputlogin = input()
        print('Enter the password of this service (Example: &%^#^@!555$#@!):')
        inputpassword = input()
        print('Enter data to database... please wait')
        Registration(inputservice, inputlogin, inputpassword)
    
    def TerminalRemover():
        print('Enter the ID for remove:')
        deleteid = int(input())
        Remover(deleteid)

    def TerminalGenerator():
        print('Enter the lenght of password:')
        lenght = int(input())
        print('Do you need a specifical numbers? (Y/N)')
        try:
            choicespecific = input()
        except choicespecific not in ['Y', 'y', 'N', 'n']:
            print('Invalid input')
        Generatorpass(lenght, choicespecific)
        
            
    

