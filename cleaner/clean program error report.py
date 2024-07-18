import os
import shutil

def clean_programs_error_report():
    # Specifica il percorso della directory da svuotare
    directory = os.path.expandvars(r'%LOCALAPPDATA%\ElevatedDiagnostics')

    # Verifica se la directory esiste
    if os.path.exists(directory):
        # Elimina tutti i file e le sottocartelle nella directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Elimina il file
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Elimina la directory e tutto il suo contenuto
            except PermissionError as e:
                print(f'Accesso negato durante l\'eliminazione del file {file_path}. Eccezione: {e}')
            except Exception as e:
                print(f'Errore durante l\'eliminazione del file {file_path}. Eccezione: {e}')
        print('Pulizia della directory Programs Error Report completata.')
    else:
        print(f'La directory {directory} non esiste')

# Chiamata alla funzione
clean_programs_error_report()
