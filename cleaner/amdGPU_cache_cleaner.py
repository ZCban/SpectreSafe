import os
import shutil

def clear_amd_cache():
    # Ottieni il percorso della directory principale dell'utente corrente
    user_home = os.path.expanduser('~')
    base_cache_path = os.path.join(user_home, "AppData", "Local", "AMD")

    # Percorsi della cache
    dx_cache_path = os.path.join(base_cache_path, "DxCache")
    ogl_cache_path = os.path.join(base_cache_path, "OglCache")
    vk_cache_path = os.path.join(base_cache_path, "VkCache")

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
                        print(f"Errore nella rimozione forse serve a sistema {file_path}")
        else:
            print(f"La cartella {cache_path} non esiste")

    # Cancella le cache
    clear_cache(dx_cache_path)
    clear_cache(ogl_cache_path)
    clear_cache(vk_cache_path)

if __name__ == "__main__":
    clear_amd_cache()
    print("Pulizia della cache AMD completata.")
