import os
import shutil

def pulisci_file_recenti():
    """
    Cancella tutti i file nella cartella dei file recenti in Esplora File su Windows.
    """
    # Ottiene il percorso della directory dei file recenti
    percorso_recenti = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Recent')

    # Verifica se la directory esiste
    if os.path.exists(percorso_recenti):
        # Elimina tutti i file nella cartella Recent
        for file_name in os.listdir(percorso_recenti):
            file_path = os.path.join(percorso_recenti, file_name)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)
                    print(f'File eliminato: {file_path}')
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f'Directory eliminata: {file_path}')
            except Exception as e:
                print(f'Errore durante l\'eliminazione di {file_path}: {e}')
    else:
        print(f'La directory {percorso_recenti} non esiste o non è accessibile.')

# Esegue la funzione per pulire i file recenti
pulisci_file_recenti()
