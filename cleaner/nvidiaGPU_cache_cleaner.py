import os
import shutil
import time
import subprocess


def nvidia_dxcache():
    # Specifica il percorso della directory da svuotare
    directory = os.path.expandvars(r'%AppData%\..\LocalLow\NVIDIA\PerDriverVersion\DXCache')

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
            except Exception as e:
                if "[WinError 32]" in str(e):
                    print(f'Non elimino, serve al sistema: {file_path}')
                else:
                    print(f'Errore durante l\'eliminazione del file {file_path}. Eccezione: {e}')
        print('Pulizia dxcache completata.')
    else:
        print(f'La directory {directory} non esiste')

def nvidia_glcache():
    # Specifica il percorso della directory da svuotare
    directory = os.path.expandvars(r'%AppData%\..\Local\NVIDIA\GLCache')

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
            except Exception as e:
                print(f'Errore durante l\'eliminazione del file {file_path}. Eccezione: {e}')
        print('Pulizia glcache completata.')
    else:
        print(f'La directory {directory} non esiste')

nvidia_dxcache()
nvidia_glcache()
