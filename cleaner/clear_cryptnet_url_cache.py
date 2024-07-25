import os
import shutil

def clear_cryptnet_url_cache():
    # Percorso della cache CryptnetUrlCache
    directory = os.path.expandvars(r'%LocalAppData%\..\LocalLow\Microsoft\CryptnetUrlCache')

    if os.path.exists(directory):
        for root, dirs, files in os.walk(directory):
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    os.unlink(file_path)
                except Exception as e:
                    print(f'Errore durante l\'eliminazione del file {file_path}. Eccezione: {e}')
            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    shutil.rmtree(dir_path)
                except Exception as e:
                    print(f'Errore durante l\'eliminazione della directory {dir_path}. Eccezione: {e}')
        print(f'Pulizia della CryptnetUrlCache completata.')
    else:
        print(f'La directory {directory} non esiste')

# Esegui la pulizia della CryptnetUrlCache
clear_cryptnet_url_cache()
