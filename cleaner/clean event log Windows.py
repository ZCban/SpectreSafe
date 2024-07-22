import subprocess
import logging

# Setup logging
logging.basicConfig(filename='clear_event_logs_log.txt', level=logging.INFO, format='%(asctime)s [EVENT_LOG_CLEAR] %(message)s')

def clear_event_logs():
    logs_to_clear = ['System', 'Security', 'Application']
    
    for log in logs_to_clear:
        try:
            command = ['wevtutil', 'cl', log]
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            logging.info(f"Successfully cleared {log} log.")
            print(f"Successfully cleared {log} log.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error clearing {log} log: {e.stderr}")
            print(f"Error clearing {log} log: {e.stderr}")

if __name__ == "__main__":
    clear_event_logs()
