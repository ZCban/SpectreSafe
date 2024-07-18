import os

def clear_amd_cache():
    # Ottieni il nome dell'utente corrente
    user_name = os.getlogin()

    # Percorsi della cache
    dx_cache_path = f"C:\\Users\\{user_name}\\AppData\\Local\\AMD\\DxCache"
    ogl_cache_path = f"C:\\Users\\{user_name}\\AppData\\Local\\AMD\\OglCache"
    vk_cache_path = f"C:\\Users\\{user_name}\\AppData\\Local\\AMD\\VkCache"

    # Funzione per cancellare i file all'interno di una cartella
    def clear_cache(cache_path):
        if os.path.exists(cache_path):
            for root, dirs, files in os.walk(cache_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        print(f"File rimosso: {file_path}")
                    except Exception as e:
                        print(f"Errore nella rimozione del file {file_path}: {e}")
        else:
            print(f"La cartella {cache_path} non esiste")

    # Cancella le cache
    clear_cache(dx_cache_path)
    clear_cache(ogl_cache_path)
    clear_cache(vk_cache_path)



clear_amd_cache()
