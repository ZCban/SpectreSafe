import os
import glob

def trova_e_elimina_file_etl(directory_di_partenza='C:\\'):
    """
    Cerca e elimina tutti i file con estensioni .etl, .evt, e .evtx nella directory specificata e nelle sottodirectory.

    Args:
    directory_di_partenza (str): Il percorso della directory di partenza. Default è 'C:\\' per l'intero disco C:.
    """
    # Estensioni di file da cercare
    estensioni = ['.etl', '.evt', '.evtx']
    file_da_eliminare = []

    # Trova tutti i file con le estensioni specificate nella directory e nelle sottodirectory
    for estensione in estensioni:
        percorso_file = os.path.join(directory_di_partenza, '**', f'*{estensione}')
        file_da_eliminare.extend(glob.glob(percorso_file, recursive=True))

    # Elimina i file trovati
    for file in file_da_eliminare:
        try:
            os.remove(file)
            print(f'File eliminato: {file}')
        except Exception as e:
            print(f'Errore durante l\'eliminazione di {file}: {e}')

def trova_e_elimina_file_dump_xml(directory_di_partenza='C:\\'):
    """
    Cerca e elimina tutti i file con estensioni .dmp e .xml nella directory specificata e nelle sottodirectory.

    Args:
    directory_di_partenza (str): Il percorso della directory di partenza. Default è 'C:\\' per l'intero disco C:.
    """
    # Estensioni di file da cercare
    estensioni = ['.dmp', '.xml']
    file_da_eliminare = []

    # Trova tutti i file con le estensioni specificate nella directory e nelle sottodirectory
    for estensione in estensioni:
        percorso_file = os.path.join(directory_di_partenza, '**', f'*{estensione}')
        file_da_eliminare.extend(glob.glob(percorso_file, recursive=True))

    # Elimina i file trovati
    for file in file_da_eliminare:
        try:
            os.remove(file)
            print(f'File eliminato: {file}')
        except Exception as e:
            print(f'Errore durante l\'eliminazione di {file}: {e}')

# Chiamata delle funzioni con la directory di partenza impostata su C:
trova_e_elimina_file_etl('C:\\')
trova_e_elimina_file_dump_xml('C:\\')

