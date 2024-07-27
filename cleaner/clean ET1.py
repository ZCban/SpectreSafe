import os
import glob

def trova_e_elimina_file_etl(directory_di_partenza='C:\\'):
    """
    Cerca e elimina tutti i file con estensione .etl nella directory specificata e nelle sottodirectory.

    Args:
    directory_di_partenza (str): Il percorso della directory di partenza. Default è 'C:\\' per l'intero disco C:.
    """
    # Trova tutti i file .etl nella directory e nelle sottodirectory
    percorso_file = os.path.join(directory_di_partenza, '**', '*.etl')
    file_da_eliminare = glob.glob(percorso_file, recursive=True)

    # Elimina i file trovati
    for file in file_da_eliminare:
        try:
            os.remove(file)
            print(f'File eliminato: {file}')
        except Exception as e:
            print(f'Errore durante l\'eliminazione di {file}: {e}')

# Chiamata della funzione con la directory di partenza impostata su C:
trova_e_elimina_file_etl('C:\\')
