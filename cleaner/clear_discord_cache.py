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

def clear_discord_caches():
    # Percorsi delle cache di Discord
    cache_directories = [
        os.path.expandvars(r'%AppData%\Discord\Cache'),
        os.path.expandvars(r'%AppData%\Discord\Code Cache'),
        os.path.expandvars(r'%AppData%\Discord\GPUCache'),
    ]

    for directory in cache_directories:
        print(f'Pulizia della cache di Discord: {directory}')
        clear_directory(directory)

# Esegui la pulizia delle cache di Discord
clear_discord_caches()
