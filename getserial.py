import os
import subprocess
import tempfile
from datetime import datetime
import requests
import socket
import winreg
import random
import logging
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
    arp_output = subprocess.getoutput('arp -a')
    for line in arp_output.split('\n'):
        if 'Internet Address' in line or 'Interface' in line or line.strip() == '':
            continue
        parts = line.split()
        ip_address, mac_address, type = parts[0], parts[1], parts[2]
        if ip_address.startswith('192.168.') and type.lower() == 'dynamic':
            return ip_address, mac_address
    return None, None

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

# Function to get specific registry data
def get_registry_data():
    key = winreg.HKEY_LOCAL_MACHINE
    registry_data = {
        r"SOFTWARE\Microsoft\Windows NT\CurrentVersion": ["InstallationID", "ProductID"],
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

# Function to get USB device information
def get_usb_devices():
    result = subprocess.run(['wmic', 'path', 'Win32_PnPEntity', 'where', 'PNPDeviceID like "USB%"', 'get', 'PNPDeviceID,Name'], capture_output=True, text=True)
    lines = result.stdout.splitlines()[1:]  # Ignore header line
    devices = []

    for line in lines:
        if line.strip():  # Ignore empty lines
            parts = line.split()
            name = " ".join(parts[:-1])  # Device name
            pnp_id = parts[-1]           # PNPDeviceID
            match = re.search(r'VID_([0-9A-F]{4})&PID_([0-9A-F]{4})', pnp_id)
            if match:
                vid = match.group(1)
                pid = match.group(2)
                devices.append((name, vid, pid))

    usb_output = ""
    for name, vid, pid in devices:
        usb_output += f"Name: {name}, VID: 0x{vid}, PID: 0x{pid}\n"
    return usb_output

OUTPUT_FILE = "getSerial_py.txt"
current_username = os.getlogin()
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(OUTPUT_FILE, "w") as output_file:
    output_file.write(f"Autore: {current_username}\n")
    output_file.write(f"Data e ora di creazione: {current_datetime}\n\n")
    
    output_file.write("ComputerSystem Name:\n")
    output_file.write(subprocess.getoutput("wmic computersystem get name"))

    output_file.write("\n\nUser Accounts (filtered):\n")
    user_accounts = subprocess.getoutput("wmic useraccount get name,sid")
    output_file.write(user_accounts)

    output_file.write("\n\nBIOS Serial Number:\n")
    output_file.write(subprocess.getoutput("wmic bios get serialnumber"))

    output_file.write("\n\nCPU Serial Number:\n")
    output_file.write(subprocess.getoutput("wmic cpu get serialnumber"))

    output_file.write("\n\nSystem Enclosure Serial Number:\n")
    output_file.write(subprocess.getoutput("wmic systemenclosure get serialnumber"))

    output_file.write("\n\nBaseBoard Serial Numbers:\n")
    output_file.write(subprocess.getoutput("wmic baseboard get serialnumber"))

    output_file.write("\n\nMemory Chip Serial Numbers:\n")
    output_file.write(subprocess.getoutput("wmic memorychip get serialnumber"))

    output_file.write("\n\nDisk Drive SERIAL NUMBER:\n")
    output_file.write(subprocess.getoutput("wmic diskdrive get model,serialnumber"))

    output_file.write("\n\nDisk Serial Partition:\n")
    output_file.write(subprocess.getoutput("vol C:"))
    output_file.write(subprocess.getoutput("vol D:"))
    output_file.write(subprocess.getoutput("vol E:"))

    output_file.write("\n\nNetwork Adapter Information:\n")
    output_file.write(subprocess.getoutput('wmic nic where "NetConnectionStatus=2" get Name,macaddress'))

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
