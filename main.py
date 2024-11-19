from menus.terminal import Terminal
import os
from config.config import *

if __name__ == '__main__':
    settingsfile = open(settings_path)
    if settings.get('terminalmenu', True):
        Terminal.menu1()
    else:
        print('In Development...')