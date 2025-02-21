import os
import subprocess
import tempfile
from datetime import datetime
import requests
import socket
import winreg
import re

# Function to get the public IP address
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except Exception as e:
        return f"Error getting public IP address: {e}"

# Function to get the router's MAC address
def get_router_mac_address():
    try:
        arp_output = subprocess.getoutput('arp -a')
        for line in arp_output.split('\n'):
            # Continue past headers or empty lines
            if 'Interface' in line or line.strip() == '':
                continue
            parts = line.split()
            # Ensure there are at least 3 parts to unpack (IP, MAC, and Type)
            if len(parts) < 3:
                continue  # Skip lines that don't have enough data
            ip_address, mac_address, type = parts[0], parts[1], parts[2]
            # Look for a dynamic entry typically associated with a router in a home network
            if ip_address.startswith('192.168.') and type.lower() == 'dynamic' or type.lower() == 'dinamico' :
                return ip_address, mac_address
    except Exception as e:
        return f"Error in getting router MAC address: {e}"
    return None, None  # Return None if no suitable entry was found

# Function to get the local IP address
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    finally:
        s.close()
    return local_ip

# Function to get Microsoft accounts
def get_microsoft_accounts():
    try:
        with tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix='.txt') as temp_file:
            temp_file_path = temp_file.name

        batch_script = f"""
        @echo off
        net user > "{temp_file_path}"
        """
        
        batch_file_path = os.path.join(tempfile.gettempdir(), 'get_users.bat')
        with open(batch_file_path, 'w') as batch_file:
            batch_file.write(batch_script)

        subprocess.run(['powershell', '-Command', 'Start-Process', 'cmd.exe', '-ArgumentList', f"/c {batch_file_path}", '-Verb', 'RunAs'])

        with open(temp_file_path, 'r') as temp_file:
            users_output = temp_file.read()

        users_lines = users_output.splitlines()
        start_listing = False
        accounts = []
        
        for line in users_lines:
            if '----------------' in line:
                start_listing = not start_listing
                continue
            if start_listing and line.strip():
                accounts.append(line.strip())
        
        microsoft_accounts = [acc for acc in accounts if '@' in acc]
        
        if microsoft_accounts:
            result = "Microsoft accounts on the system:\n" + "\n".join(microsoft_accounts) + "\n"
        else:
            result = "No Microsoft accounts on the system.\n"
        
        os.remove(temp_file_path)
        os.remove(batch_file_path)
        
        return result
    
    except Exception as e:
        return f"An error occurred: {e}"

# Function to get registry value
def get_registry_value(key, subkey, value_name):
    try:
        registry_key = winreg.OpenKey(key, subkey, 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, value_name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None

def get_registry_value(key, subkey, value_name):
    try:
        with winreg.OpenKey(key, subkey) as registry_key:
            value, regtype = winreg.QueryValueEx(registry_key, value_name)
            return value
    except FileNotFoundError:
        return "Not found"
    except Exception as e:
        return f"Error: {e}"

def get_registry_data():
    key = winreg.HKEY_LOCAL_MACHINE
    registry_data = {
        r"SOFTWARE\Microsoft\Windows NT\CurrentVersion": ["InstallationID", "ProductID", "BuildGUID", "RegisteredOrganization", "RegisteredOwner"],
        r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform": ["BackupProductKeyDefault"],
        r"SOFTWARE\Microsoft\SQMClient": ["MachineId"],
        r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001": ["HwProfileGuid", "BIOSReleaseDate", "BIOSVersion", "ComputerHardwareId"],
        r"SOFTWARE\Microsoft\Cryptography": ["MachineGuid"],
        r"SYSTEM\CurrentControlSet\Control\Nsi\{eb004a03-9b1a-11d4-9123-0050047759bc}\26": ["VariableId"],
        r"HARDWARE\DESCRIPTION\System\BIOS": ["SystemFamily", "SystemManufacturer", "SystemProductName", "SystemSKU", "SystemVersion", "BaseBoardManufacturer", "BaseBoardProduct", "BaseBoardVersion", "BIOSReleaseDate", "BIOSVendor"],
        r"SOFTWARE\NVIDIA Corporation\Global": ["ClientUUID"],
        r"SOFTWARE\NVIDIA Corporation\Global\CoProcManager": ["ChipsetMatchID"],
    }

    registry_output = ""
    for subkey, values in registry_data.items():
        for value_name in values:
            value = get_registry_value(key, subkey, value_name)
            registry_output += f"{value_name}: {value}\n"
    return registry_output



def get_usb_devices():
    # Comando PowerShell per ottenere dispositivi USB
    cmd = ["powershell", "Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -like '*USB*' } | Select-Object InstanceId, FriendlyName"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def get_network_mac_address():
    try:
        output = subprocess.getoutput("getmac /fo csv /v")
        lines = output.splitlines()
        mac_addresses = []

        for line in lines:
            parts = line.replace('"', '').split(',')
            if len(parts) > 2:
                mac_address = parts[1].strip()
                name = parts[2].strip()
                if mac_address and mac_address != 'N/A':
                    mac_addresses.append(f"{name}  {mac_address}")

        if mac_addresses:
            mac_output = "\n".join(mac_addresses) + "\n"
        else:
            mac_output = "No MAC addresses found.\n"
        
        return mac_output
    except Exception as e:
        return f"Error getting network MAC addresses: {e}"

def get_volume_info(drive_letter):
    try:
        # Esegue il comando vol per il drive specificato
        result = subprocess.getoutput(f"vol {drive_letter}:")
        if "Impossibile trovare il percorso specificato" in result:
            # Gestisce il caso in cui il volume non è presente
            return f"{drive_letter}: Drive not found.\n"
        else:
            return f"{drive_letter}: {result}\n"
    except Exception as e:
        # Gestisce eventuali eccezioni durante l'esecuzione del comando
        return f"{drive_letter}: Error retrieving volume information: {str(e)}\n"

OUTPUT_FILE = "getSerial_py.txt"
current_username = os.getlogin()
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Funzione per eseguire i comandi PowerShell e ottenere l'output
def run_powershell_command(command):
    return subprocess.getoutput(f"powershell -Command \"{command}\"")

with open(OUTPUT_FILE, "w") as output_file:
    output_file.write(f"Autore: {current_username}\n")
    output_file.write(f"Data e ora di creazione: {current_datetime}\n\n")
    
    # Ottiene il nome del sistema
    output_file.write("ComputerSystem Name:\n")
    cs_name = run_powershell_command("Get-ComputerInfo -Property CsName")
    output_file.write(cs_name + "\n\n")
    
    # Ottiene gli account utente
    output_file.write("User Accounts (filtered):\n")
    user_accounts = run_powershell_command("Get-LocalUser | Select-Object Name, SID | Format-Table -HideTableHeaders")
    output_file.write(user_accounts + "\n\n")
    
    # Ottiene il numero di serie del BIOS
    output_file.write("BIOS Serial Number:\n")
    bios_serial = run_powershell_command("Get-WmiObject Win32_BIOS | Select-Object SerialNumber | Format-Table -HideTableHeaders")
    output_file.write(bios_serial + "\n\n")
    
    # Ottiene il numero di serie della CPU (CPU ID)
    output_file.write("CPU Serial Number:\n")
    cpu_serial = run_powershell_command("Get-WmiObject Win32_Processor | Select-Object ProcessorId | Format-Table -HideTableHeaders")
    output_file.write(cpu_serial + "\n\n")
    
    # Ottiene il numero di serie dell'involucro del sistema
    output_file.write("System Enclosure Serial Number:\n")
    system_enclosure_serial = run_powershell_command("Get-WmiObject Win32_SystemEnclosure | Select-Object SerialNumber | Format-Table -HideTableHeaders")
    output_file.write(system_enclosure_serial + "\n\n")
    
    # Ottiene i numeri di serie della scheda madre
    output_file.write("BaseBoard Serial Numbers:\n")
    baseboard_serial = run_powershell_command("Get-WmiObject Win32_BaseBoard | Select-Object SerialNumber | Format-Table -HideTableHeaders")
    output_file.write(baseboard_serial + "\n\n")
    
    # Ottiene i numeri di serie dei chip di memoria
    output_file.write("Memory Chip Serial Numbers:\n")
    memory_chip_serial = run_powershell_command("Get-WmiObject Win32_PhysicalMemory | Select-Object SerialNumber | Format-Table -HideTableHeaders")
    output_file.write(memory_chip_serial + "\n\n")
    
    # Ottiene i numeri di serie dei dischi rigidi
    output_file.write("Disk Drive SERIAL NUMBER:\n")
    disk_drive_serial = run_powershell_command("Get-WmiObject Win32_DiskDrive | Select-Object Model, SerialNumber | Format-Table -HideTableHeaders")
    output_file.write(disk_drive_serial + "\n")

    # Scrive le informazioni sulle partizioni dei dischi
    output_file.write("Disk Serial Partition:\n")
    output_file.write(get_volume_info('C'))
    output_file.write(get_volume_info('D'))
    output_file.write(get_volume_info('E'))
    output_file.write(get_volume_info('F'))
    output_file.write(get_volume_info('G'))
    output_file.write("\n")

    public_ip = get_public_ip()
    output_file.write(f"Indirizzo IP pubblico: {public_ip}\n\n")

    local_ip = get_local_ip()
    output_file.write(f"Indirizzo IP locale: {local_ip}\n\n")

    router_ip, router_mac = get_router_mac_address()
    if router_mac:
        output_file.write(f"Indirizzo IP del router: {router_ip}\n")
        output_file.write(f"Indirizzo MAC del router: {router_mac}\n\n")
    else:
        output_file.write("Indirizzo MAC del router non trovato.\n\n")

    output_file.write("\n\nMAC Addresses:\n")
    output_file.write(get_network_mac_address())

    output_file.write("\n\nNVIDIA GPU UUID Information:\n")
    output_file.write(subprocess.getoutput('nvidia-smi --query-gpu=gpu_name,uuid --format=csv'))

    powershell_command = 'PowerShell -Command "Get-WmiObject -Namespace root\wmi -Class WmiMonitorID | ForEach-Object { [System.Text.Encoding]::ASCII.GetString($_.SerialNumberID) }"'
    output_file.write("\n\nMonitor dysp Serial Numbers:\n")
    output_file.write(subprocess.getoutput(powershell_command))

    powershell_command = 'PowerShell -Command "Get-TpmEndorsementKeyInfo -Hash "Sha256"'
    output_file.write("\nTpmEndorsementKeyInfo:\n")
    output_file.write(subprocess.getoutput(powershell_command))

    output_file.write("\n\nMicrosoft Accounts:\n")
    output_file.write(get_microsoft_accounts())

    output_file.write("\n\nRegistry Data:\n")
    output_file.write(get_registry_data())

    output_file.write("\n\nUSB Devices:\n")
    output_file.write(get_usb_devices())


print(f"Results have been saved to {OUTPUT_FILE}")

