from menus.terminal import Terminal
from menus.pyqt import PyQTInterface
import os
from config.config import *

if __name__ == '__main__':
    settingsfile = open(settings_path)

    if not settings.get('terminalmenu', True):
        PyQTInterface().run()
    else:
        Terminal.run()