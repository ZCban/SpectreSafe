import winreg
import os

def list_and_remove_autostart_apps():
    autostart_apps = []

    registry_paths = [
        (winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run'),
        (winreg.HKEY_LOCAL_MACHINE, r'Software\Microsoft\Windows\CurrentVersion\Run'),
        (winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\RunOnce'),
        (winreg.HKEY_LOCAL_MACHINE, r'Software\Microsoft\Windows\CurrentVersion\RunOnce')
    ]

    for hkey, path in registry_paths:
        try:
            registry_key = winreg.OpenKey(hkey, path, 0, winreg.KEY_READ | winreg.KEY_WRITE)
            i = 0
            while True:
                try:
                    app_name, app_path, _ = winreg.EnumValue(registry_key, i)
                    autostart_apps.append((app_name, app_path))
                    winreg.DeleteValue(registry_key, app_name)
                    i += 1
                except OSError:
                    break
            winreg.CloseKey(registry_key)
        except Exception as e:
            print(f"Error reading/removing autostart applications from {path}: {e}")

    folder_paths = [
        os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup'),
        os.path.join(os.getenv('ProgramData'), r'Microsoft\Windows\Start Menu\Programs\Startup')
    ]

    for folder_path in folder_paths:
        try:
            if os.path.exists(folder_path):
                for item in os.listdir(folder_path):
                    item_path = os.path.join(folder_path, item)
                    if os.path.isfile(item_path) and item.lower() != 'desktop.ini':
                        autostart_apps.append((item, item_path))
                        os.remove(item_path)
        except Exception as e:
            print(f"Error reading/removing autostart applications from {folder_path}: {e}")

    return autostart_apps

# Example usage
apps = list_and_remove_autostart_apps()
for app in apps:
    print(f"Removed Application Name: {app[0]}")




