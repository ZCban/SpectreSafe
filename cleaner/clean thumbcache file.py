import os

def delete_thumbcache_files(directory):
    deleted_files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith('thumbcache'):
                file_path = os.path.join(root, filename)
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                    print(f"Deleted: {file_path}")
                except FileNotFoundError:
                    print(f"File not found: {file_path}")
                except PermissionError:
                    print(f"Permission denied: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
    return deleted_files

# Specifica la directory
thumbcache_directory = 'C:\\Users\\FBposta\\AppData\\Local\\Microsoft\\Windows\\Explorer'

# Elimina i file thumbcache e salva il report
deleted_files = delete_thumbcache_files(thumbcache_directory)

# Scrivi il report su un file di testo
report_file = 'deleted_thumbcache_files_report.txt'
with open(report_file, 'w') as report:
    for file in deleted_files:
        report.write(f"Deleted: {file}\n")

print(f"Report saved to {report_file}")
