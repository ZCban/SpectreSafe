import os
import subprocess

def run_python_files_in_cleaner():
    # Ottieni il percorso della directory corrente
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Costruisci il percorso della cartella "cleaner"
    cleaner_directory = os.path.join(current_directory, 'cleaner')
    
    # Controlla se la cartella "cleaner" esiste
    if not os.path.isdir(cleaner_directory):
        print(f"La cartella {cleaner_directory} non esiste.")
        return
    
    # Elenca tutti i file nella cartella "cleaner"
    files = os.listdir(cleaner_directory)
    
    # Filtra solo i file con estensione .py
    python_files = [file for file in files if file.endswith('.py')]
    
    # Esegui ciascun file Python uno alla volta
    for python_file in python_files:
        file_path = os.path.join(cleaner_directory, python_file)
        print(f"Eseguendo {python_file}...")
        subprocess.run(['python', file_path])


run_python_files_in_cleaner()
