import os

settings_path = os.path.join(os.path.dirname(__file__), 'settings.txt')

settings = {}

def load_settings(settings_path):
    with open(settings_path, 'r') as file:
        for line in file:
            line = line.rstrip()
            if line and '=' in line:
                key, value = line.split('=', 1)
                if value.lower() in ['true', 'false']:
                    settings[key.strip()] = value.lower() == 'true'
                else:
                    settings[key.strip()] = value.strip().upper()
    return settings

def save_settings(settings_path, settings):
    print(f"[DEBUG] Saving settings to {settings_path}")
    print(f"[DEBUG] Settings to save: {settings}")
    try:
        current_settings = {}
        try:
            with open(settings_path, 'r') as file:
                for line in file:
                    line = line.rstrip()
                    if line and '=' in line:
                        key, value = line.split('=', 1)
                        current_settings[key.strip()] = value.strip()
        except FileNotFoundError:
            pass

        for key, value in settings.items():
            if key not in current_settings:
                current_settings[key] = value

        with open(settings_path, 'w') as file:
            for key, value in current_settings.items():
                print(f"[DEBUG] Writing: {key}={value}")
                file.write(f"{key}={value}\n")
        print("[DEBUG] Settings saved successfully")
    except Exception as e:
        print(f"[DEBUG] Error saving settings: {e}")
        traceback.print_exc()

load_settings(settings_path)

locale = {}

language = settings.get('language', 'EN')
if language == 'RU':
    locale['Choice'] = 'RU'
elif language == 'EN':
    locale['Choice'] = 'EN'
else:
    locale['Choice'] = 'EN'