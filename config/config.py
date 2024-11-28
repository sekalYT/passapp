import os

settings_path = os.path.join(os.path.dirname(__file__), 'settings.txt')

settings = {}

def load_settings(settings_path):
    with open(settings_path, 'r') as file:
        for line in file:
            line = line.rstrip()
            if line and '=' in line:
                key, value = line.split('=', 1)
                settings[key.strip()] = value.strip().upper()
    return settings

def save_settings(settings_path, settings):
    with open(settings_path, 'w') as file:
        for key, value in settings.items():
            file.write(f"{key}={value}\n")

load_settings(settings_path)

locale = {}

language = settings.get('language', 'EN')
if language == 'RU':
    locale['Choice'] = 'RU'
elif language == 'EN':
    locale['Choice'] = 'EN'
else:
    locale['Choice'] = 'EN'