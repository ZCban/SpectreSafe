import os
import shutil

def delete_wer_files():
    # Percorso alla cartella WER
    wer_path = r'C:\ProgramData\Microsoft\Windows\WER'

    # Verifica se la cartella WER esiste
    if os.path.exists(wer_path):
        # Itera su ogni cartella all'interno di WER
        for root, dirs, files in os.walk(wer_path):
            for file in files:
                # Costruisci il percorso completo del file
                file_path = os.path.join(root, file)
                try:
                    # Elimina il file
                    os.remove(file_path)
                    print(f'Eliminato: {file_path}')
                except Exception as e:
                    print(f'Errore nell\'eliminazione di {file_path}: {e}')
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    # Elimina la cartella vuota
                    os.rmdir(dir_path)
                    print(f'Eliminata cartella: {dir_path}')
                except Exception as e:
                    print(f'Errore nell\'eliminazione della cartella {dir_path}: {e}')

        # Svuota il Cestino (Recycle Bin)
        try:
            os.system('rd /s /q %systemdrive%$Recycle.Bin')
            print('Cestino svuotato.')
        except Exception as e:
            print(f'Errore nello svuotamento del Cestino: {e}')
    else:
        print(f'La cartella WER non esiste al percorso {wer_path}')

# Esegui la funzione
delete_wer_files()
