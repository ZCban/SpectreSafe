import os

def find_log_files(start_dir):
    log_files = []
    for root, _, filenames in os.walk(start_dir):
        for filename in filenames:
            if filename.endswith(('.log', '.LOG2', '.LOG1')):
                log_files.append(os.path.join(root, filename))
    return log_files

def delete_log_files(log_files, report_file):
    with open(report_file, 'w') as report:
        for log_file in log_files:
            try:
                os.remove(log_file)
                report.write(f"Deleted: {log_file}\n")
                print(f"Deleted: {log_file}")
            except FileNotFoundError:
                report.write(f"File not found: {log_file}\n")
                print(f"File not found: {log_file}")
            except PermissionError:
                report.write(f"Permission denied: {log_file}\n")
                print(f"Permission denied: {log_file}")
            except Exception as e:
                report.write(f"Error deleting {log_file}: {e}\n")
                print(f"Error deleting {log_file}: {e}")

start_directory = 'C:\\'
log_files = find_log_files(start_directory)

# Stampa i file trovati
print('File di log trovati:')
for log_file in log_files:
    print(log_file)

# Elimina i file di log e scrivi il report
report_file = 'deleted_log_files_report.txt'
delete_log_files(log_files, report_file)
print(f"Report saved to {report_file}")

