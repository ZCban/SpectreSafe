import os
import shutil

def delete_item(path):
    """
    Funzione ausiliaria per eliminare un file o una cartella specificata.

    Args:
    path (str): Percorso del file o della cartella.
    """
    try:
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        print(f"Pulizia di {path} completata.")
    except Exception as e:
        print(f'Errore durante l\'eliminazione di {path}. Motivo: {e}')

def clear_browser_data():
    """
    Funzione per cancellare i dati di diversi browser.
    Cerca automaticamente le cartelle nel profilo utente corrente.
    """
    user_profile_path = os.environ['USERPROFILE']

    # Percorsi della cartella Cache e altri dati dei browser
    brave_paths = {
        'cache': os.path.join(user_profile_path, r'AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Cache\Cache_Data'),
        'cookies': os.path.join(user_profile_path, r'AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Cookies'),
        'history': os.path.join(user_profile_path, r'AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\History'),
        'session': os.path.join(user_profile_path, r'AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Sessions'),
        'downloads': os.path.join(user_profile_path, r'AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Download Metadata')
    }

    chrome_paths = {
        'cache': os.path.join(user_profile_path, r'AppData\Local\Google\Chrome\User Data\Default\Cache'),
        'cookies': os.path.join(user_profile_path, r'AppData\Local\Google\Chrome\User Data\Default\Cookies'),
        'history': os.path.join(user_profile_path, r'AppData\Local\Google\Chrome\User Data\Default\History'),
        'session': os.path.join(user_profile_path, r'AppData\Local\Google\Chrome\User Data\Default\Sessions'),
        'downloads': os.path.join(user_profile_path, r'AppData\Local\Google\Chrome\User Data\Default\Download Metadata')
    }

    firefox_profile_path = os.path.join(user_profile_path, r'AppData\Local\Mozilla\Firefox\Profiles')
    
    edge_paths = {
        'cache': os.path.join(user_profile_path, r'AppData\Local\Microsoft\Edge\User Data\Default\Cache'),
        'cookies': os.path.join(user_profile_path, r'AppData\Local\Microsoft\Edge\User Data\Default\Cookies'),
        'history': os.path.join(user_profile_path, r'AppData\Local\Microsoft\Edge\User Data\Default\History'),
        'session': os.path.join(user_profile_path, r'AppData\Local\Microsoft\Edge\User Data\Default\Sessions'),
        'downloads': os.path.join(user_profile_path, r'AppData\Local\Microsoft\Edge\User Data\Default\Download Metadata')
    }
    
    opera_paths = {
        'cache': os.path.join(user_profile_path, r'AppData\Roaming\Opera Software\Opera Stable\Cache'),
        'cookies': os.path.join(user_profile_path, r'AppData\Roaming\Opera Software\Opera Stable\Cookies'),
        'history': os.path.join(user_profile_path, r'AppData\Roaming\Opera Software\Opera Stable\History'),
        'session': os.path.join(user_profile_path, r'AppData\Roaming\Opera Software\Opera Stable\Sessions'),
        'downloads': os.path.join(user_profile_path, r'AppData\Roaming\Opera Software\Opera Stable\Download Metadata')
    }

    # Chiama la funzione ausiliaria per ciascun tipo di dato e browser
    for browser, paths in [('Brave', brave_paths), ('Chrome', chrome_paths), ('Edge', edge_paths), ('Opera', opera_paths)]:
        for data_type, path in paths.items():
            delete_item(path)

    # Firefox gestisce i dati in modo diverso
    if os.path.exists(firefox_profile_path):
        for profile in os.listdir(firefox_profile_path):
            profile_path = os.path.join(firefox_profile_path, profile)
            firefox_paths = {
                'cache': os.path.join(profile_path, 'cache2'),
                'cookies': os.path.join(profile_path, 'cookies.sqlite'),
                'history': os.path.join(profile_path, 'places.sqlite'),
                'session': os.path.join(profile_path, 'sessionstore-backups'),
                'downloads': os.path.join(profile_path, 'downloads.sqlite')
            }
            for data_type, path in firefox_paths.items():
                delete_item(path)
    else:
        print(f"Cartella profili Firefox non trovata in {firefox_profile_path}.")



clear_browser_data()
