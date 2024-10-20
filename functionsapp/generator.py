import random
import string

class Generatorpass():
    def __init__(self, lenght, choicespecific):
        self.lenght = lenght
        self.choicespecific = choicespecific
        self.mainlogic()
    
    def mainlogic(self):
        if self.choicespecific == 'Y' or self.choicespecific == 'y':
            password_characters = string.ascii_letters + string.digits + string.punctuation
            print(''.join(random.choice(password_characters) for i in range(self.lenght)))
        else:
            password_characters = string.ascii_letters + string.digits
            print(''.join(random.choice(password_characters) for i in range(self.lenght)))
