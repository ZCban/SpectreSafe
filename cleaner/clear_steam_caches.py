import os
import shutil

def clear_directory(directory):
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Errore durante l\'eliminazione del file {file_path}. Eccezione: {e}')
        print(f'Pulizia della directory {directory} completata.')
    else:
        print(f'La directory {directory} non esiste')

def clear_steam_caches():
    # Percorsi delle cache di Steam
    steam_path = os.path.expandvars(r'%ProgramFiles(x86)%\Steam')
    cache_directories = [
        os.path.join(steam_path, 'appcache'),
        os.path.join(steam_path, 'config'),
        os.path.join(steam_path, 'htmlcache'),
        os.path.join(steam_path, 'steamapps', 'downloading'),
        os.path.join(steam_path, 'depotcache'),
        os.path.join(steam_path, 'logs')  # Aggiunta della cartella Logs
    ]

    for directory in cache_directories:
        print(f'Pulizia della cache di Steam: {directory}')
        clear_directory(directory)

# Esegui la pulizia delle cache di Steam
clear_steam_caches()

