import os
import shutil

def pulisci_directory(percorso_directory):
    """
    Pulisce tutti i file e le sottodirectory all'interno della directory specificata.
    
    Args:
    percorso_directory (str): Il percorso della directory da pulire.
    """
    # Verifica che la directory esista
    if os.path.exists(percorso_directory):
        # Scorri attraverso tutti i file nella directory
        for filename in os.listdir(percorso_directory):
            file_path = os.path.join(percorso_directory, filename)
            try:
                # Verifica se il percorso è un file o un link simbolico e lo elimina
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                    print(f"File {file_path} eliminato con successo.")
                # Verifica se il percorso è una directory e la elimina
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"Directory {file_path} eliminata con successo.")
            except Exception as e:
                print(f"Errore durante l'eliminazione di {file_path}: {e}")
    else:
        print(f"La directory {percorso_directory} non esiste.")

# Esempio di utilizzo
pulisci_directory(r"C:\Users\dd\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine")
