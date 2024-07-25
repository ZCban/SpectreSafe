import os
import shutil

def clear_directory(directory):
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Errore durante l\'eliminazione del file {file_path}. Eccezione: {e}')
        print(f'Pulizia della directory {directory} completata.')
    else:
        print(f'La directory {directory} non esiste')

def clear_intel_shader_cache():
    # Cache degli shader Intel
    intel_cache_dirs = [
        os.path.expandvars(r'%LocalAppData%\..\LocalLow\Intel\ShaderCache'),
        os.path.expandvars(r'%LocalAppData%\..\LocalLow\Intel\DxCache')
    ]
    for directory in intel_cache_dirs:
        print(f'Pulizia della cache degli shader Intel: {directory}')
        clear_directory(directory)

def clear_amd_shader_cache():
    # Cache degli shader AMD
    amd_cache_dirs = [
        os.path.expandvars(r'%LocalAppData%\AMD\DxCache'),
        os.path.expandvars(r'%LocalAppData%\AMD\GLCache')
    ]
    for directory in amd_cache_dirs:
        print(f'Pulizia della cache degli shader AMD: {directory}')
        clear_directory(directory)

def detect_and_clear_cache():
    # Verifica della presenza di cache specifiche per Intel e AMD
    intel_present = os.path.exists(os.path.expandvars(r'%LocalAppData%\..\LocalLow\Intel\ShaderCache'))
    amd_present = os.path.exists(os.path.expandvars(r'%LocalAppData%\AMD\DxCache'))

    if intel_present:
        print("Sistema con GPU Intel rilevato.")
        clear_intel_shader_cache()
    elif amd_present:
        print("Sistema con GPU AMD rilevato.")
        clear_amd_shader_cache()
    else:
        print("Nessuna cache specifica per Intel o AMD trovata.")

# Esegui il rilevamento e la pulizia
detect_and_clear_cache()
