import os
import shutil

def svuota_d3dscache():
    percorso_cache = os.path.join(os.getenv('LOCALAPPDATA'), 'D3DSCache')
    
    if os.path.exists(percorso_cache):
        # Itera sui file e sottocartelle all'interno della cartella D3DSCache
        for elemento in os.listdir(percorso_cache):
            percorso_elemento = os.path.join(percorso_cache, elemento)
            try:
                if os.path.isfile(percorso_elemento) or os.path.islink(percorso_elemento):
                    os.unlink(percorso_elemento)
                elif os.path.isdir(percorso_elemento):
                    shutil.rmtree(percorso_elemento)
            except Exception as e:
                print(f"Errore durante la rimozione di {percorso_elemento}: {e}")
    else:
        print(f"La cartella {percorso_cache} non esiste.")

svuota_d3dscache()
