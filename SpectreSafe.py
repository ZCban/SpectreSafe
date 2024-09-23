import winreg
import uuid
import random
import string
import os
import subprocess
import logging
import re
import datetime
import time
import ctypes
import struct
import tempfile
import json
from ctypes import wintypes

TEXTSIZE = 256
MAX_EDID_BLOCKS = 4
MAX_EDID_EXTENSION_BLOCKS = 1

# Percorso della cartella di log
log_folder = 'log'
log_file_path = os.path.join(log_folder, 'spoofer_log.txt')

# Crea la cartella di log se non esiste
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Verifica se il file di log esiste già e lo elimina se presente
if os.path.exists(log_file_path):
    os.remove(log_file_path)

# Configura il logging per creare un nuovo file di log nella cartella specificata
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s [SPOOFER] %(message)s')

class Spoofer:
    def write_log(message):
        logging.info(message)
        print(message)
    
    @staticmethod
    def log_change(operation, old_value, new_value):
        log_message = f"{operation} Changed from {old_value} to {new_value}"
        print(log_message)  # Print to console
        logging.info(log_message)  # Log to file

    class PowerShellExecutionPolicyManager:
        @staticmethod
        def allow_script_pw():
            try:
                # Ottiene la politica di esecuzione corrente per la macchina locale
                current_policy_command = ["powershell.exe", "-Command", "Get-ExecutionPolicy -Scope LocalMachine"]
                current_policy = subprocess.check_output(current_policy_command).decode().strip()

                # Controlla se la politica corrente non è 'Unrestricted'
                if current_policy != 'Unrestricted':
                    # Imposta la politica di esecuzione su 'Unrestricted'
                    set_policy_command = ["powershell.exe", "-Command", "Set-ExecutionPolicy Unrestricted -Scope LocalMachine -Force"]
                    subprocess.run(set_policy_command, check=True)
                    print("PS ExecutionPolicy cambiata in Unrestricted.")
                else:
                    print("PS ExecutionPolicy è già Unrestricted.")
            except subprocess.CalledProcessError as e:
                print(f"Errore durante il cambiamento della ExecutionPolicy: {e}")
            except Exception as e:
                print(f"Errore imprevisto: {e}")

    class BuildGUID:
        @staticmethod
        def generate_build_guid():
            part1 = random.randint(100000000, 999999999)
            part2 = random.randint(1000000000, 4294967295)  # Max value for a 32-bit unsigned int
            part3 = random.randint(100000000, 999999999)
            return f"{part1}-{part2}-{part3}"

        @staticmethod
        def spoof():
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", 0, winreg.KEY_ALL_ACCESS) as key:
                    old_value, _ = winreg.QueryValueEx(key, "BuildGUID")
                    new_value = Spoofer.BuildGUID.generate_build_guid()
                    winreg.SetValueEx(key, "BuildGUID", 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change("BuildGUID", old_value, new_value)
                    return True
            except Exception as e:
                logging.error(f"Error modifying BuildGUID: {e}")
                return False

    class RegisteredOrganization:
        @staticmethod
        def generate_organization_id():
            part1 = ''.join(random.choices('0123456789', k=9))
            part2 = ''.join(random.choices('0123456789', k=9))
            part3 = ''.join(random.choices('0123456789', k=9))
            return f"{part1}-{part2}-{part3}"

        @staticmethod
        def spoof():
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", 0, winreg.KEY_ALL_ACCESS) as key:
                    old_value, _ = winreg.QueryValueEx(key, "RegisteredOrganization")
                    new_value = Spoofer.RegisteredOrganization.generate_organization_id()
                    winreg.SetValueEx(key, "RegisteredOrganization", 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change("RegisteredOrganization", old_value, new_value)
                    return True
            except Exception as e:
                logging.error(f"Error modifying RegisteredOrganization: {e}")
                return False


    class DigitalProductId:
        @staticmethod
        def spoof():
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", 0, winreg.KEY_ALL_ACCESS) as key:
                    old_value, _ = winreg.QueryValueEx(key, "DigitalProductId")
                    if len(old_value) >= 5:
                        new_value = bytearray(old_value)
                        old_bytes = old_value[-5:]
                        for i in range(5):
                            new_value[-1 - i] = random.randint(0, 255)
                        winreg.SetValueEx(key, "DigitalProductId", 0, winreg.REG_BINARY, new_value)
                        new_bytes = new_value[-5:]
                        Spoofer.log_change("DigitalProductId", old_bytes, new_bytes)
                    return True
            except Exception as e:
                logging.error(f"Error modifying DigitalProductId: {e}")
                return False

    class DigitalProductId4:
        @staticmethod
        def spoof():
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", 0, winreg.KEY_ALL_ACCESS) as key:
                    old_value, _ = winreg.QueryValueEx(key, "DigitalProductId4")
                    if len(old_value) >= 5:
                        new_value = bytearray(old_value)
                        old_bytes = old_value[-5:]
                        for i in range(5):
                            new_value[-1 - i] = random.randint(0, 255)
                        winreg.SetValueEx(key, "DigitalProductId4", 0, winreg.REG_BINARY, new_value)
                        new_bytes = new_value[-5:]
                        Spoofer.log_change("DigitalProductId4", old_bytes, new_bytes)
                    return True
            except Exception as e:
                logging.error(f"Error modifying DigitalProductId4: {e}")
                return False


    class MachineId:
        @staticmethod
        def spoof():
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\SQMClient", 0, winreg.KEY_ALL_ACCESS) as key:
                    old_value, _ = winreg.QueryValueEx(key, "MachineId")
                    new_value = "{" + str(uuid.uuid4()) + "}"
                    winreg.SetValueEx(key, "MachineId", 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change("MachineId", old_value, new_value)
                    return True
            except Exception as e:
                logging.error(f"Error modifying MachineId: {e}")
                return False

    class HardwareGUID:
        @staticmethod
        def spoof():
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001", 0, winreg.KEY_ALL_ACCESS) as key:
                    old_value, _ = winreg.QueryValueEx(key, "HwProfileGuid")
                    new_value = "{" + str(uuid.uuid4()) + "}"
                    winreg.SetValueEx(key, "HwProfileGuid", 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change("HwProfileGuid", old_value, new_value)
                    return True
            except Exception as e:
                logging.error(f"Error modifying HwProfileGuid: {e}")
                return False

    class MachineGUID:
        @staticmethod
        def spoof():
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Cryptography", 0, winreg.KEY_ALL_ACCESS) as key:
                    old_value, _ = winreg.QueryValueEx(key, "MachineGuid")
                    new_value = str(uuid.uuid4())
                    winreg.SetValueEx(key, "MachineGuid", 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change("MachineGuid", old_value, new_value)
                    return True
            except Exception as e:
                logging.error(f"Error modifying MachineGuid: {e}")
                return False

    class EFIVariables:
        @staticmethod
        def spoof():
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\Nsi\\{eb004a03-9b1a-11d4-9123-0050047759bc}\\26", 0, winreg.KEY_ALL_ACCESS) as key:
                    try:
                        old_value, _ = winreg.QueryValueEx(key, "VariableId")
                    except FileNotFoundError:
                        old_value = "Not Set"
                    new_value = str(uuid.uuid4())
                    winreg.SetValueEx(key, "EFIVariables", 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change("EFIVariables", old_value, new_value)
                    return True
            except Exception as e:
                logging.error(f"Error accessing EFI Variables in the Registry: {e}")
                return False

    class SystemInfo:
        @staticmethod
        def RandomId(length):
            characters = string.ascii_letters + string.digits
            return ''.join(random.choice(characters) for _ in range(length))

        @staticmethod
        def spoof():
            key_path = "SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001"
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
                    # Modify BIOSReleaseDate
                    try:
                        old_bios_date, _ = winreg.QueryValueEx(key, "BIOSReleaseDate")
                    except FileNotFoundError:
                        old_bios_date = "Not Set"
                    new_bios_date = f"{random.randint(1, 28)}/{random.randint(1, 12)}/{random.randint(2000, 2023)}"
                    winreg.SetValueEx(key, "BIOSReleaseDate", 0, winreg.REG_SZ, new_bios_date)
                    Spoofer.log_change("BIOSReleaseDate", old_bios_date, new_bios_date)

                    # Modify BIOSVersion
                    try:
                        old_bios_version, _ = winreg.QueryValueEx(key, "BIOSVersion")
                    except FileNotFoundError:
                        old_bios_version = "Not Set"
                    new_bios_version = Spoofer.SystemInfo.RandomId(5)
                    winreg.SetValueEx(key, "BIOSVersion", 0, winreg.REG_SZ, new_bios_version)
                    Spoofer.log_change("BIOSVersion", old_bios_version, new_bios_version)

                    # Modify ComputerHardwareId
                    try:
                        old_hardware_id, _ = winreg.QueryValueEx(key, "ComputerHardwareId")
                    except FileNotFoundError:
                        old_hardware_id = "Not Set"

                    new_hardware_id = f"{{{uuid.uuid4()}}}"
                    winreg.SetValueEx(key, "ComputerHardwareId", 0, winreg.REG_SZ, new_hardware_id)
                    Spoofer.log_change("ComputerHardwareId", old_hardware_id, new_hardware_id)

                    return True
            except Exception as e:
                logging.error(f"Error modifying SystemInfo: {e}")
                return False

    class SystemInfoExtended:
        @staticmethod
        def random_id(length):
            characters = string.digits
            return ''.join(random.choice(characters) for _ in range(length))

        @staticmethod
        def spoof():
            try:
                # Paths for system and BIOS information in the registry
                system_info_key_path = "HARDWARE\\DESCRIPTION\\System"
                bios_info_key_path = "HARDWARE\\DESCRIPTION\\System\\BIOS"

                # Spoofing system information
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, bios_info_key_path, 0, winreg.KEY_ALL_ACCESS) as system_key:
                    value_name = "SystemFamily"
                    old_value = Spoofer.SystemInfoExtended.get_current_value(system_key, value_name)
                    new_value = Spoofer.SystemInfoExtended.random_id(14)
                    winreg.SetValueEx(system_key, value_name, 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change(value_name, old_value, new_value)
                
                # Spoofing system information
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, bios_info_key_path, 0, winreg.KEY_ALL_ACCESS) as system_key:
                    value_name = "SystemManufacturer"
                    old_value = Spoofer.SystemInfoExtended.get_current_value(system_key, value_name)
                    new_value = Spoofer.SystemInfoExtended.random_id(14)
                    winreg.SetValueEx(system_key, value_name, 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change(value_name, old_value, new_value)

                # Spoofing system information
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, bios_info_key_path, 0, winreg.KEY_ALL_ACCESS) as system_key:
                    value_name = "SystemProductName"
                    old_value = Spoofer.SystemInfoExtended.get_current_value(system_key, value_name)
                    new_value = Spoofer.SystemInfoExtended.random_id(14)
                    winreg.SetValueEx(system_key, value_name, 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change(value_name, old_value, new_value)

                # Spoofing system information
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, bios_info_key_path, 0, winreg.KEY_ALL_ACCESS) as system_key:
                    value_name = "SystemSKU"
                    old_value = Spoofer.SystemInfoExtended.get_current_value(system_key, value_name)
                    new_value = Spoofer.SystemInfoExtended.random_id(14)
                    winreg.SetValueEx(system_key, value_name, 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change(value_name, old_value, new_value)

                # Spoofing system information   
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, bios_info_key_path, 0, winreg.KEY_ALL_ACCESS) as system_key:
                    value_name = "SystemVersion"
                    old_value = Spoofer.SystemInfoExtended.get_current_value(system_key, value_name)
                    new_value = Spoofer.SystemInfoExtended.random_id(14)
                    winreg.SetValueEx(system_key, value_name, 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change(value_name, old_value, new_value)

                # Spoofing Board information
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, bios_info_key_path, 0, winreg.KEY_ALL_ACCESS) as bios_key:
                    value_name = "BaseBoardManufacturer"
                    old_value = Spoofer.SystemInfoExtended.get_current_value(bios_key, value_name)
                    new_value = Spoofer.SystemInfoExtended.random_id(14)
                    winreg.SetValueEx(bios_key, value_name, 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change(value_name, old_value, new_value)

                # Spoofing Board information
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, bios_info_key_path, 0, winreg.KEY_ALL_ACCESS) as bios_key:
                    value_name = "BaseBoardProduct"
                    old_value = Spoofer.SystemInfoExtended.get_current_value(bios_key, value_name)
                    new_value = Spoofer.SystemInfoExtended.random_id(14)
                    winreg.SetValueEx(bios_key, value_name, 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change(value_name, old_value, new_value)

                # Spoofing Board information
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, bios_info_key_path, 0, winreg.KEY_ALL_ACCESS) as bios_key:
                    value_name = "BaseBoardVersion"
                    old_value = Spoofer.SystemInfoExtended.get_current_value(bios_key, value_name)
                    new_value = Spoofer.SystemInfoExtended.random_id(14)
                    winreg.SetValueEx(bios_key, value_name, 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change(value_name, old_value, new_value)

                # Spoofing Board information
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, bios_info_key_path, 0, winreg.KEY_ALL_ACCESS) as bios_key:
                    value_name = "BIOSReleaseDate"
                    old_value = Spoofer.SystemInfoExtended.get_current_value(bios_key, value_name)
                    new_value = f"{random.randint(1, 28)}/{random.randint(1, 12)}/{random.randint(2000, 2023)}"
                    winreg.SetValueEx(bios_key, value_name, 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change(value_name, old_value, new_value)

                # Spoofing Board information
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, bios_info_key_path, 0, winreg.KEY_ALL_ACCESS) as bios_key:
                    value_name = "BIOSVendor"
                    old_value = Spoofer.SystemInfoExtended.get_current_value(bios_key, value_name)
                    new_value = Spoofer.SystemInfoExtended.random_id(14)
                    winreg.SetValueEx(bios_key, value_name, 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change(value_name, old_value, new_value)

                return True
            except Exception as e:
                logging.error(f"Error modifying extended SystemInfo: {e}")
                return False

        @staticmethod
        def get_current_value(key, value_name):
            try:
                return winreg.QueryValueEx(key, value_name)[0]
            except FileNotFoundError:
                return "Not Set"

    class ProductId:
        @staticmethod
        def get_value():
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", 0, winreg.KEY_READ) as key:
                    value, _ = winreg.QueryValueEx(key, "ProductId")
                    return value
            except Exception as e:
                logging.error(f"Error reading ProductId: {e}")
                return "Error"

        @staticmethod
        def spoof():
            old_value = Spoofer.ProductId.get_value()
            new_value = "{}-{}-{}-{}".format(
                ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)),
                ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)),
                ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)),
                ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)))
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", 0, winreg.KEY_WRITE) as key:
                    winreg.SetValueEx(key, "ProductId", 0, winreg.REG_SZ, new_value)
                    Spoofer.log_change("ProductId", old_value, new_value)
                    return True
            except Exception as e:
                logging.error(f"Error modifying ProductId: {e}")
                return False
    class OSInstallDate:
        @staticmethod
        def spoof():
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", 0, winreg.KEY_ALL_ACCESS) as key:
                    old_value, _ = winreg.QueryValueEx(key, "InstallDate")
                    new_value = int(time.time()) - random.randint(0, 10**8)
                    winreg.SetValueEx(key, "InstallDate", 0, winreg.REG_DWORD, new_value)
                    Spoofer.log_change("InstallDate", old_value, new_value)
                    return True
            except Exception as e:
                logging.error(f"Error modifying InstallDate: {e}")
                return False

    class InstallationID:
        @staticmethod
        def spoof():
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", 0, winreg.KEY_ALL_ACCESS) as key:
                    # Attempt to read the old InstallationID value. If it doesn't exist, use a placeholder.
                    try:
                        old_value, _ = winreg.QueryValueEx(key, "InstallationID")
                    except FileNotFoundError:
                        old_value = "Not Set"

                    newInstallationID = str(uuid.uuid4())
                    winreg.SetValueEx(key, "InstallationID", 0, winreg.REG_SZ, newInstallationID)
                    # Log the change of InstallationID.
                    Spoofer.log_change("InstallationID", old_value, newInstallationID)
                    return True
            except Exception as e:
                logging.error(f"Error modifying InstallationID: {e}")
                return False

    class ComputerUserRenamer:
        @staticmethod
        def generate_random_name(length=12):
            charset = string.ascii_letters + string.digits
            return ''.join(random.choice(charset) for _ in range(length))

        @staticmethod
        def execute_command(command):
            try:
                result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return result.stdout.decode().strip()
            except subprocess.CalledProcessError as e:
                return e.stderr.decode().strip()

        @staticmethod
        def spoof():
            try:
                # Ottieni il nome corrente del computer
                current_computer_name_command = "wmic computersystem get name"
                current_computer_name = Spoofer.ComputerUserRenamer.execute_command(current_computer_name_command).split('\n')[1]

                # Ottieni il nome utente corrente
                current_user_name_command = "whoami"
                current_user_name = Spoofer.ComputerUserRenamer.execute_command(current_user_name_command).split('\\')[-1]

                new_computer_name = Spoofer.ComputerUserRenamer.generate_random_name()
                new_user_name = Spoofer.ComputerUserRenamer.generate_random_name()

                # Rinomina il computer
                rename_computer_command = f"wmic computersystem where name='{current_computer_name}' rename {new_computer_name}"
                computer_rename_result = Spoofer.ComputerUserRenamer.execute_command(rename_computer_command)

                # Rinomina l'account utente
                rename_user_command = f"wmic useraccount where name='{current_user_name}' rename {new_user_name}"
                user_rename_result = Spoofer.ComputerUserRenamer.execute_command(rename_user_command)

                # Log changes
                Spoofer.log_change("ComputerName", current_computer_name, new_computer_name)
                Spoofer.log_change("UserName", current_user_name, new_user_name)

                return True
            except Exception as e:
                logging.error(f"Error renaming computer/user: {e}")
                return False

    class NvidiaSettings:
        @staticmethod
        def modify_registry_ClientUUID():
            key_path = r"SOFTWARE\NVIDIA Corporation\Global"
            value_name = "ClientUUID"

            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ | winreg.KEY_WRITE) as key:
                    original_value, _ = winreg.QueryValueEx(key, value_name)
                    original_value_str = original_value

                    new_byte1, new_byte2 = random.randint(0, 255), random.randint(0, 255)
                    new_value_str = original_value_str[:-5] + "{:02X}".format(new_byte1) + "{:02X}".format(new_byte2) + "}"

                    winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_value_str)
                    Spoofer.log_change("ClientUUID", original_value_str, new_value_str)
                    return True
            except Exception as e:
                logging.error(f"Error modifying ClientUUID: {e}")
                return False

        @staticmethod
        def modify_registry_ChipsetMatchID():
            key_path = r"SOFTWARE\NVIDIA Corporation\Global\CoProcManager"
            value_name = "ChipsetMatchID"

            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ | winreg.KEY_WRITE) as key:
                    original_value, _ = winreg.QueryValueEx(key, value_name)
                    original_value_str = original_value

                    new_value_str = original_value_str[:-4] + ''.join(random.choices('0123456789', k=4))

                    winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_value_str)
                    Spoofer.log_change("ChipsetMatchID", original_value_str, new_value_str)
                    return True
            except Exception as e:
                logging.error(f"Error modifying ChipsetMatchID: {e}")
                return False

    @staticmethod
    def generate_random_key(format_key):
        def random_hex(n):
            return ''.join(random.choices('0123456789ABCDEF', k=n))

        pattern = re.sub(r'[A-F0-9]', 'X', format_key)  # Replace all hex digits with 'X'
        random_key = ''.join(random_hex(1) if ch == 'X' else ch for ch in pattern)
        return random_key

    class RenameDiskSpoofer:
        @staticmethod
        def spoof():
            try:
                drives = Spoofer.VolumeSerialNumberSpoofer.get_available_drives()
                for drive in drives:
                    new_label = Spoofer.SystemInfo.RandomId(12)
                    command = f"label {drive}: {new_label}"
                    subprocess.run(command, shell=True, check=True)
                    logging.info(f"Changed volume label of {drive}: to {new_label}")
                    return True
            except Exception as e:
                logging.error(f"Error changing disk volume labels: {e}")
                return False

    class DiskSpoofer:
        @staticmethod
        def run_diskpart_commands(commands):
            process = subprocess.Popen('diskpart', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, error = process.communicate(input="\n".join(commands))
            if process.returncode != 0:
                logging.error(f"DiskPart Error: {error}")
            return output

        @staticmethod
        def list_disks_and_spoof_unique_ids():
            list_disks_output = Spoofer.DiskSpoofer.run_diskpart_commands(['list disk'])
            disk_indices = re.findall(r'Disk (\d+)', list_disks_output)

            for index in disk_indices:
                unique_id_output = Spoofer.DiskSpoofer.run_diskpart_commands([
                    f'select disk {index}',
                    'uniqueid disk'
                ])
                current_unique_id_match = re.search(r'Disk ID: (.*)', unique_id_output)
                if not current_unique_id_match:
                    logging.error(f"Could not find unique ID for disk {index}")
                    continue
                current_unique_id = current_unique_id_match.group(1).strip()
                Spoofer.log_change(f"Current Disk {index} Unique ID", current_unique_id, "")

                disk_info_output = Spoofer.DiskSpoofer.run_diskpart_commands([
                    f'select disk {index}',
                    'detail disk'
                ])
                is_system_disk = re.search(r'Boot.*Yes', disk_info_output, re.IGNORECASE) is not None

                if not is_system_disk:
                    new_uuid = Spoofer.generate_random_key(current_unique_id)
                    
                    # Ensure no braces in the new UUID
                    new_uuid = new_uuid.replace("{", "").replace("}", "")
                    
                    print(new_uuid)
                    
                    spoof_output = Spoofer.DiskSpoofer.run_diskpart_commands([
                        f'select disk {index}',
                        f'uniqueid disk ID={new_uuid}'
                    ])
                    
                    logging.info(f"Disk {index} spoof output: {spoof_output}")

                    verification_output = Spoofer.DiskSpoofer.run_diskpart_commands([
                        f'select disk {index}',
                        'uniqueid disk'
                    ])
                    verified_unique_id_match = re.search(r'Disk ID: (.*)', verification_output)
                    if not verified_unique_id_match:
                        logging.error(f"Could not verify new unique ID for disk {index}")
                        continue
                    verified_unique_id = verified_unique_id_match.group(1).strip()

                    Spoofer.log_change(f"Disk {index} Unique ID", current_unique_id, verified_unique_id)
                else:
                    logging.info(f"Disk {index} is the system disk. Skipping unique GUID spoofing.")

    class MacAddressSpoofer:
        @staticmethod
        def spoof():
            ps_script_content = """
            # Percorso del file di log aggiornato
            $logFilePath = "C:\\Users\\Admin\\Desktop\\logfile.txt"

            # Metodo per cambiare il MAC address di un adattatore di rete nel registro di sistema
            function Change-MacAddressInRegistry {
                param (
                    [Parameter(Mandatory=$true)]
                    [Microsoft.Management.Infrastructure.CimInstance]$adapter
                )
                
                try {
                    # Legge il vecchio indirizzo MAC
                    $oldMAC = $adapter.MacAddress
                    # Lista di descrizioni di adattatori specifici per il cambio MAC
                    $targetDescriptions = @("TAP-NordVPN Windows Provider V9", "TAP-NordVPN Windows Adapter V9")
                
                    if ($adapter.InterfaceDescription -in $targetDescriptions) {
                        $validPrefixes = @("02", "06", "0A", "0E", "12")
                        $prefix = $validPrefixes | Get-Random
                        $newDigits = -join ((48..57) + (65..70) | Get-Random -Count 10 | ForEach-Object { [char]$_ })
                        $newMAC = ($prefix + $newDigits.Substring(0,10)) -replace '(.{2})', '$1-' -replace '-$',''
                    } else {
                        $newDigits = -join ((48..57) + (65..70) | Get-Random -Count 4 | ForEach-Object { [char]$_ })
                        $newMAC = $oldMAC.Substring(0,12) +  $newDigits.Substring(0,2) + '-' + $newDigits.Substring(2,2)
                    }
                    
                    Write-Host "Generato nuovo MAC per $($adapter.Name): $newMAC"

                    # Disabilita la scheda di rete prima di apportare modifiche al registro
                    Disable-NetAdapter -Name $adapter.Name -Confirm:$false
                    Write-Host "Scheda $($adapter.Name) disabilitata"

                    # Verifica della chiave di registro
                    $registryPath = "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}"
                    $adapterDescription = $adapter.InterfaceDescription

                    # Scansione delle sottochiavi alla ricerca di una corrispondenza con la descrizione dell'adattatore
                    Get-ChildItem -Path $registryPath | ForEach-Object {
                        $subKey = $_.PSChildName
                        $subKeyPath = Join-Path -Path $registryPath -ChildPath $subKey
                        $driverDesc = Get-ItemProperty -Path $subKeyPath -Name "DriverDesc" -ErrorAction SilentlyContinue

                        if ($driverDesc.DriverDesc -eq $adapterDescription) {
                            Write-Host "Trovata chiave di registro per l'adattatore $($adapter.Name) con descrizione: $adapterDescription"

                            # Creazione dei valori stringa NetworkAddress e MAC
                            New-ItemProperty -Path $subKeyPath -Name "NetworkAddress" -Value $newMAC -PropertyType "String" -Force | Out-Null
                            New-ItemProperty -Path $subKeyPath -Name "MAC" -Value $newMAC -PropertyType "String" -Force | Out-Null

                            Write-Host "Valori di registro 'NetworkAddress' e 'MAC' creati per $adapterDescription"

                            $logEntry = "Data: $(Get-Date) | Scheda di rete: $($adapter.Name) | Vecchio indirizzo MAC: $oldMAC | Nuovo indirizzo MAC: $newMAC | Modificato nel registro"
                            Add-Content -Path $logFilePath -Value $logEntry
                        }
                    }

                    # Riabilita la scheda di rete per applicare la modifica
                    Enable-NetAdapter -Name $adapter.Name -Confirm:$false
                    Write-Host "Scheda $($adapter.Name) riabilitata"

                    # Verifica se il nuovo MAC è attivo
                    $activeMacs = (getmac | Select-String -Pattern '([0-9A-F]{2}-){5}[0-9A-F]{2}' -AllMatches).Matches | ForEach-Object { $_.Value }
                    if ($activeMacs -contains $newMAC) {
                        Write-Host "Nuovo MAC $newMAC verificato con successo per $($adapter.Name)."
                        # Registra l'operazione nel file di log
                        $logEntry = "Data: $(Get-Date) | Scheda di rete: $($adapter.Name) | Nuovo indirizzo MAC $newMAC verificato con successo."
                        Add-Content -Path $logFilePath -Value $logEntry
                    } else {
                        Write-Host "Errore: Nuovo MAC $newMAC non trovato per la scheda $($adapter.Name)."
                        # Registra l'errore nel file di log
                        $logEntry = "Data: $(Get-Date) | Scheda di rete: $($adapter.Name) | Errore: Nuovo MAC $newMAC non trovato. Il cambio MAC potrebbe non essere riuscito."
                        Add-Content -Path $logFilePath -Value $logEntry
                    }
                } catch {
                    Write-Host "Errore durante il tentativo di cambiare il MAC address per $($adapter.Name): $_"
                    $logEntry = "Data: $(Get-Date) | Scheda di rete: $($adapter.Name) | Errore: $_"
                    Add-Content -Path $logFilePath -Value $logEntry
                }
            }

            # Esegui il comando Getmac e memorizza i risultati filtrati
            $macAddresses = Getmac | Where-Object { $_ -notmatch "N/D" }

            # Estrai solo gli indirizzi MAC dalla lista filtrata
            $macList = $macAddresses -replace "\\s+.*", ""

            # Ottieni le informazioni sugli adattatori di rete corrispondenti agli indirizzi MAC filtrati
            $netAdapters = Get-NetAdapter | Where-Object { $macList -contains $_.MacAddress }

            # Applica il cambiamento del MAC address solo agli adattatori filtrati
            foreach ($adapter in $netAdapters) {
                try {
                    Change-MacAddressInRegistry -adapter $adapter
                } catch {
                    Write-Host "Errore durante il cambio del MAC per $($adapter.Name): $_"
                    $logEntry = "Data: $(Get-Date) | Scheda di rete: $($adapter.Name) | Errore durante il cambio del MAC: $_"
                    Add-Content -Path $logFilePath -Value $logEntry
                }
            }

            # Flush DNS, reset IP, reset Winsock, and clear ARP cache
            Write-Host "Eseguendo flush DNS, reset IP, reset Winsock, e clear ARP cache..."
            ipconfig /flushdns
            netsh int ip reset
            netsh winsock reset
            netsh interface ip delete arpcache
            """

            # Imposta il percorso e il nome del file dello script PowerShell
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            ps_script_filename = "manage_devices.ps1"
            ps_script_path = os.path.join(desktop_path, ps_script_filename)

            # Scrive lo script PowerShell in un file
            with open(ps_script_path, "w") as ps_script_file:
                ps_script_file.write(ps_script_content)

            # Comando per eseguire lo script PowerShell come amministratore
            run_as_admin_command = [
                "powershell.exe",
                "-NoProfile",
                "-ExecutionPolicy", "Bypass",
                "-Command", f"Start-Process powershell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File \"{ps_script_path}\"' -Verb RunAs"
            ]

            # Esegue lo script PowerShell come amministratore
            try:
                subprocess.run(run_as_admin_command, shell=True, check=True)
                logging.info("MAC address spoofing script executed successfully.")
                time.sleep(10)  # Attendere un po' più a lungo per assicurarsi che il file di log sia scritto

                # Legge e logga il contenuto del file di log
                log_file_path = os.path.join(desktop_path, "logfile.txt")
                if os.path.exists(log_file_path):
                    with open(log_file_path, "r") as log_file:
                        log_contents = log_file.read()
                        logging.info("Log file contents:\n" + log_contents)
                else:
                    logging.warning("Log file not found.")
                return True
            except Exception as e:
                logging.error(f"Error executing MAC address spoofing script: {e}")
                return False
            finally:
                os.remove(ps_script_path)
                if os.path.exists(log_file_path):
                    os.remove(log_file_path)

    class VolumeSerialNumberSpoofer:
        GENERIC_READ = 0x80000000
        GENERIC_WRITE = 0x40000000
        FILE_SHARE_READ = 0x00000001
        FILE_SHARE_WRITE = 0x00000002
        OPEN_EXISTING = 0x00000003
        INVALID_HANDLE_VALUE = -1
        SECTOR_SIZE = 512

        class PartialBootSectorInfo:
            def __init__(self, fs, fs_offs, serial_offs):
                self.fs = fs
                self.fs_offs = fs_offs
                self.serial_offs = serial_offs

        @staticmethod
        def log_message(message):
            logging.info(message)

        @staticmethod
        def open_disk(drive):
            return ctypes.windll.kernel32.CreateFileW(
                drive,
                Spoofer.VolumeSerialNumberSpoofer.GENERIC_READ | Spoofer.VolumeSerialNumberSpoofer.GENERIC_WRITE,
                Spoofer.VolumeSerialNumberSpoofer.FILE_SHARE_READ | Spoofer.VolumeSerialNumberSpoofer.FILE_SHARE_WRITE,
                None,
                Spoofer.VolumeSerialNumberSpoofer.OPEN_EXISTING,
                0,
                None
            )

        @staticmethod
        def read_sector(handle, sector_number):
            sector_offset = sector_number * Spoofer.VolumeSerialNumberSpoofer.SECTOR_SIZE
            ctypes.windll.kernel32.SetFilePointerEx(handle, ctypes.c_int64(sector_offset), None, 0)
            buffer = ctypes.create_string_buffer(Spoofer.VolumeSerialNumberSpoofer.SECTOR_SIZE)
            bytes_read = ctypes.c_ulong(0)
            success = ctypes.windll.kernel32.ReadFile(handle, buffer, Spoofer.VolumeSerialNumberSpoofer.SECTOR_SIZE, ctypes.byref(bytes_read), None)
            return success, buffer.raw

        @staticmethod
        def write_sector(handle, sector_number, buffer):
            sector_offset = sector_number * Spoofer.VolumeSerialNumberSpoofer.SECTOR_SIZE
            ctypes.windll.kernel32.SetFilePointerEx(handle, ctypes.c_int64(sector_offset), None, 0)
            bytes_written = ctypes.c_ulong(0)
            success = ctypes.windll.kernel32.WriteFile(handle, buffer, Spoofer.VolumeSerialNumberSpoofer.SECTOR_SIZE, ctypes.byref(bytes_written), None)
            return success

        @staticmethod
        def close_disk(handle):
            ctypes.windll.kernel32.CloseHandle(handle)

        @staticmethod
        def get_available_drives():
            drives = []
            drive_bitmask = ctypes.windll.kernel32.GetLogicalDrives()
            for i in range(26):
                if drive_bitmask & (1 << i):
                    drives.append(chr(65 + i))
            return drives

        @staticmethod
        def spoof_volume_serial_numbers():
            random.seed(int(time.time()))

            pbsi = [
                Spoofer.VolumeSerialNumberSpoofer.PartialBootSectorInfo("FAT32", 0x52, 0x43),
                Spoofer.VolumeSerialNumberSpoofer.PartialBootSectorInfo("FAT", 0x36, 0x27),
                Spoofer.VolumeSerialNumberSpoofer.PartialBootSectorInfo("NTFS", 0x03, 0x48)
            ]

            drives = Spoofer.VolumeSerialNumberSpoofer.get_available_drives()

            for drive in drives:
                drive_path = f"\\\\.\\{drive}:"
                #Spoofer.VolumeSerialNumberSpoofer.log_message(f"Attempting to open drive: {drive_path}")

                handle = Spoofer.VolumeSerialNumberSpoofer.open_disk(drive_path)
                if handle == Spoofer.VolumeSerialNumberSpoofer.INVALID_HANDLE_VALUE:
                    Spoofer.VolumeSerialNumberSpoofer.log_message(f"Could not open disk {drive_path}!")
                    continue

                success, sector = Spoofer.VolumeSerialNumberSpoofer.read_sector(handle, 0)
                if not success:
                    Spoofer.VolumeSerialNumberSpoofer.log_message(f"Could not read sector on disk {drive_path}!")
                    Spoofer.VolumeSerialNumberSpoofer.close_disk(handle)
                    continue

                for info in pbsi:
                    if sector[info.fs_offs:info.fs_offs + len(info.fs)] == info.fs.encode():
                        break
                else:
                    Spoofer.VolumeSerialNumberSpoofer.log_message(f"Cannot change serial number of this file system on disk {drive_path}!")
                    Spoofer.VolumeSerialNumberSpoofer.close_disk(handle)
                    continue

                new_serial = random.randint(0, 0xFFFFFFFF)
                new_serial_bytes = struct.pack("<I", new_serial)
                sector = sector[:info.serial_offs] + new_serial_bytes + sector[info.serial_offs + 4:]

                success = Spoofer.VolumeSerialNumberSpoofer.write_sector(handle, 0, sector)
                if not success:
                    Spoofer.VolumeSerialNumberSpoofer.log_message(f"Could not write sector on disk {drive_path}!")
                    Spoofer.VolumeSerialNumberSpoofer.close_disk(handle)
                    continue

                Spoofer.VolumeSerialNumberSpoofer.log_message(f"Volume serial number changed successfully for drive {drive}: to {new_serial:08X}!")
                Spoofer.VolumeSerialNumberSpoofer.close_disk(handle)

            Spoofer.VolumeSerialNumberSpoofer.log_message("Volume serial numbers changed successfully! You might want to restart your system for changes to take effect.")

    class DisplayClass:
        def __init__(self, display_id, device_id):
            size = MAX_EDID_BLOCKS * 128
            if size < 256:
                size = 256

            self.active_data = bytearray(size)
            self.override_data = bytearray(size)
            self.reset_data = bytearray(size)

            self.display_id = display_id
            self.device_id = device_id
            self.device_name = ""

            self.active = False
            self.override = False
            self.matched = False
            self.deleted = False
            self.restart = False

        def log_message(self, message):
            logging.info(message)

        def load_device_name(self):
            path = f"SYSTEM\\CurrentControlSet\\Enum\\DISPLAY\\{self.display_id}\\{self.device_id}"
            try:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
                device_desc, _ = winreg.QueryValueEx(key, "DeviceDesc")
                winreg.CloseKey(key)
                
                self.device_name = device_desc.split(';')[1] if ';' in device_desc else device_desc
                return True
            except FileNotFoundError:
                return False

        def get_active_status(self):
            guid_devinterface_monitor = ctypes.c_char_p(b"{E6F07B5F-EE97-4A90-B076-33F57BF4EAA7}")
            path = f"DISPLAY\\{self.display_id}\\{self.device_id}"
            devices = ctypes.windll.setupapi.SetupDiGetClassDevsA(guid_devinterface_monitor, path.encode('utf-8'), None, 0x12)
            if devices == ctypes.c_void_p(-1).value:
                return False

            device_info_data = ctypes.create_string_buffer(0)
            device_info_data.cbSize = ctypes.sizeof(device_info_data)
            status = ctypes.windll.setupapi.SetupDiEnumDeviceInfo(devices, 0, ctypes.byref(device_info_data))
            ctypes.windll.setupapi.SetupDiDestroyDeviceInfoList(devices)
            return bool(status)

        def load_override_data(self):
            path = f"SYSTEM\\CurrentControlSet\\Enum\\DISPLAY\\{self.display_id}\\{self.device_id}\\Device Parameters\\EDID_OVERRIDE"
            try:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
                buffer, _ = winreg.QueryValueEx(key, "0")
                if len(buffer) >= 128:
                    self.override_data[:128] = buffer[:128]
                    for block in range(1, MAX_EDID_BLOCKS):
                        try:
                            buffer, _ = winreg.QueryValueEx(key, str(block))
                            if len(buffer) >= 128:
                                self.override_data[block*128:(block+1)*128] = buffer[:128]
                        except FileNotFoundError:
                            continue
                winreg.CloseKey(key)
                return True
            except FileNotFoundError:
                return False

        def load_active_data(self):
            path = f"SYSTEM\\CurrentControlSet\\Enum\\DISPLAY\\{self.display_id}\\{self.device_id}\\Device Parameters"
            try:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
                buffer, _ = winreg.QueryValueEx(key, "EDID")
                if len(buffer) >= 128:
                    self.active_data[:len(buffer)] = buffer
                    winreg.CloseKey(key)
                    return True
            except FileNotFoundError:
                return False

        def extract_serial(self, edid_data):
            return edid_data[12:16]

        def extract_serial_number_string(self, edid_data):
            for i in range(4):
                offset = 54 + i * 18
                if edid_data[offset] == 0 and edid_data[offset + 1] == 0 and edid_data[offset + 2] == 0xFF:
                    return edid_data[offset + 5:offset + 18].decode('ascii').rstrip()
            return ""

        def set_serial_number_string(self, edid_data, serial_number):
            serial_descriptor = bytearray(18)
            serial_descriptor[0] = 0x00  # Flag for detailed timing descriptor
            serial_descriptor[3] = 0xFF  # Serial number tag
            serial_bytes = serial_number.encode('ascii')
            serial_descriptor[5:5 + len(serial_bytes)] = serial_bytes[:13]  # Serial number can be up to 13 characters
            serial_descriptor[17] = 0x0A  # Newline character

            # Place the serial number descriptor in the correct position in the EDID data
            edid_data[54:72] = serial_descriptor[:18]

        def extract_monitor_name(self, edid_data):
            for i in range(4):
                offset = 54 + i * 18
                if edid_data[offset] == 0 and edid_data[offset + 1] == 0 and edid_data[offset + 2] == 0xFC:
                    return edid_data[offset + 5:offset + 18].decode('ascii').rstrip()
            return ""

        def set_monitor_name(self, edid_data, monitor_name):
            name_descriptor = bytearray(18)
            name_descriptor[0] = 0x00  # Flag for detailed timing descriptor
            name_descriptor[3] = 0xFC  # Monitor name tag
            name_bytes = monitor_name.encode('ascii')
            name_descriptor[5:5 + len(name_bytes)] = name_bytes[:13]  # Monitor name can be up to 13 characters
            name_descriptor[17] = 0x0A  # Newline character

            # Place the name descriptor in the correct position in the EDID data
            edid_data[72:90] = name_descriptor[:18]

        def random_string(self, length):
            letters = string.ascii_uppercase + string.digits
            return ''.join(random.choice(letters) for i in range(length))

        def generate_random_edid(self, existing_edid, current_name_length):
            random_edid = bytearray(existing_edid)  # Start with the existing EDID and modify parts of it
            # Manufacturer ID (2 bytes, little-endian)
            manufacturer_id = self.random_string(2)
            random_edid[8:10] = int.from_bytes(manufacturer_id.encode('ascii'), 'little').to_bytes(2, 'little')
            # Product Code (2 bytes, little-endian)
            product_code = self.random_string(2)
            random_edid[10:12] = int.from_bytes(product_code.encode('ascii'), 'little').to_bytes(2, 'little')
            # id serial (4 bytes)
            id_serial = random.randint(0, 2**32 - 1)
            random_edid[12:16] = id_serial.to_bytes(4, 'little')
            # Week of Manufacture (1 byte)
            random_edid[16] = random.randint(1, 53)
            # Year of Manufacture (1 byte, offset from 1990)
            random_edid[17] = random.randint(0, 255)
            # Set Random Serial Number String
            random_serial = self.random_string(current_name_length)
            self.set_serial_number_string(random_edid, random_serial)
            # Set Random Monitor Name
            random_name = self.random_string(current_name_length)
            self.set_monitor_name(random_edid, random_name)
            # Checksum (1 byte)
            random_edid[127] = (-sum(random_edid[:127]) & 0xFF)
            return random_edid

        def save_override_data(self):
            path = f"SYSTEM\\CurrentControlSet\\Enum\\DISPLAY\\{self.display_id}\\{self.device_id}\\Device Parameters\\EDID_OVERRIDE"
            try:
                key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, path)
                winreg.SetValueEx(key, "0", 0, winreg.REG_BINARY, self.override_data[:128])
                for block in range(1, MAX_EDID_BLOCKS):
                    if any(self.override_data[block*128:(block+1)*128]):
                        winreg.SetValueEx(key, str(block), 0, winreg.REG_BINARY, self.override_data[block*128:(block+1)*128])
                    else:
                        try:
                            winreg.DeleteValue(key, str(block))
                        except FileNotFoundError:
                            pass
                winreg.CloseKey(key)
                return True
            except Exception as e:
                self.log_message(f"Error saving override data: {e}")
                return False

        def modify_edid(self):
            if not self.load_device_name():
                self.log_message(f"Error loading device name for Display ID: {self.display_id}, Device ID: {self.device_id}")
                return False
            self.active = self.get_active_status()
            self.override = self.load_override_data()
            if not self.load_active_data():
                self.log_message(f"Error loading active data for Display ID: {self.display_id}, Device ID: {self.device_id}")
                return False

            old_serial = self.extract_serial(self.active_data)
            current_name_length = 13  # Assuming the current name has 13 characters, adapt if necessary
            new_edid = self.generate_random_edid(self.active_data, current_name_length)
            new_serial = self.extract_serial(new_edid)
            old_serial_string = self.extract_serial_number_string(self.active_data)
            new_serial_string = self.extract_serial_number_string(new_edid)
            old_name = self.extract_monitor_name(self.active_data)
            new_name = self.extract_monitor_name(new_edid)

            self.log_message(f"Display ID: {self.display_id}, Vecchio Serial hex : {old_serial.hex()}, Nuovo Serial hex: {new_serial.hex()}")

            self.override_data = new_edid
            self.save_override_data()
            return True

    @staticmethod
    def spoof_display_edid():
        display_ids, device_ids = Spoofer.get_display_and_device_ids()
        for display_id, device_id in zip(display_ids, device_ids):
            display = Spoofer.DisplayClass(display_id, device_id)
            if display.modify_edid():
                logging.info(f"EDID modificato con successo per Display ID: {display_id}, Device ID: {device_id}")
            else:
                logging.error(f"Errore nella modifica dell'EDID per Display ID: {display_id}, Device ID: {device_id}")

    @staticmethod
    def get_display_and_device_ids():
        display_ids = []
        device_ids = []
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Enum\\DISPLAY")
            for i in range(winreg.QueryInfoKey(key)[0]):
                display_id = winreg.EnumKey(key, i)
                display_key = winreg.OpenKey(key, display_id)
                for j in range(winreg.QueryInfoKey(display_key)[0]):
                    device_id = winreg.EnumKey(display_key, j)
                    display_ids.append(display_id)
                    device_ids.append(device_id)
                winreg.CloseKey(display_key)
            winreg.CloseKey(key)
        except FileNotFoundError:
            pass
        return display_ids, device_ids

    class DMISpoofer:
        @staticmethod
        def log_message(message):
            logging.info(message)

        @staticmethod
        def generate_random_digits(length=15):
            """Generates a string of random digits of the specified length."""
            return ''.join(str(random.randint(0, 9)) for _ in range(length))

        @staticmethod
        def find_file(name, path):
            """Finds a file with the given name starting from the specified path."""
            for root, dirs, files in os.walk(path):
                if name in files:
                    return os.path.join(root, name)
            return None

        @staticmethod
        def compare_files(pre_file, post_file):
            """Compares the pre and post spoof files and logs the differences."""
            with open(pre_file, "r") as pre, open(post_file, "r") as post:
                pre_lines = pre.readlines()
                post_lines = post.readlines()

                # Log table headers
                Spoofer.DMISpoofer.log_message(f"{'Old Key':<50} | {'New Key':<50}")
                Spoofer.DMISpoofer.log_message("="*103)

                for pre_line, post_line in zip(pre_lines, post_lines):
                    if pre_line != post_line:
                        Spoofer.DMISpoofer.log_message(f"{pre_line.strip():<50} | {post_line.strip():<50}")
                        Spoofer.DMISpoofer.log_message("-"*103)

        @staticmethod
        def remove_r_done(file_path):
            """Removes 'R    Done' from the specified file."""
            with open(file_path, 'r') as file:
                lines = file.readlines()

            processed_lines = []
            for line in lines:
                processed_line = line.replace('R    Done', '').rstrip()  # Remove 'R    Done' and trailing spaces
                processed_lines.append(processed_line)

            with open(file_path, 'w') as file:
                for line in processed_lines:
                    file.write(line + '\n')

        @staticmethod
        def create_and_run_batch_file(directory, commands):
            """Creates and runs a batch file with the specified commands in the given directory."""
            # Check if the directory exists
            if not os.path.isdir(directory):
                Spoofer.DMISpoofer.log_message(f"The directory '{directory}' does not exist.")
                return

            # Change the current directory
            os.chdir(directory)

            # Create a temporary batch file
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.bat', dir=directory) as batch_file:
                for command in commands:
                    batch_file.write(command + "\n")
                # Add a command to close the cmd at the end
                batch_file.write("exit\n")
                batch_file_path = batch_file.name

            # Function to delete the batch file after execution
            def delete_temp_batch():
                os.remove(batch_file_path)

            # Execute the batch file and close the cmd after execution
            try:
                process = subprocess.Popen(["cmd", "/C", batch_file_path], close_fds=True)
                process.wait()  # Wait for the cmd process to finish
            finally:
                delete_temp_batch()  # Delete the batch file

        @staticmethod
        def spoof_dmi():
            file_to_find = "AMIDEWINx64.EXE"
            starting_path = "C:\\"  # Change this path if you want to start the search from another location

            path_to_file = Spoofer.DMISpoofer.find_file(file_to_find, starting_path)

            if path_to_file:
                Spoofer.DMISpoofer.log_message(f"Found {file_to_find} at {path_to_file}")
                path_to_directory = os.path.dirname(path_to_file)

                # Generate random digit combinations
                random_digits_SS = Spoofer.DMISpoofer.generate_random_digits()
                random_digits_BS = Spoofer.DMISpoofer.generate_random_digits()
                random_digits_BSH = Spoofer.DMISpoofer.generate_random_digits()
                random_digits_CS = Spoofer.DMISpoofer.generate_random_digits()
                random_digits_CSH = Spoofer.DMISpoofer.generate_random_digits()
                random_digits_PSN = Spoofer.DMISpoofer.generate_random_digits()
                random_digits_PBS = Spoofer.DMISpoofer.generate_random_digits()

                # Commands to run in cmd
                commands_to_run = [
                    "AMIDEWINx64.EXE /ALL pre_spoof.txt",
                    "AMIDEWINx64.EXE /SU AUTO",
                    f"AMIDEWINx64.EXE /SS {random_digits_SS}",
                    f"AMIDEWINx64.EXE /BS {random_digits_BS}",
                    f"AMIDEWINx64.EXE /BSH {random_digits_BSH}",
                    f"AMIDEWINx64.EXE /CS {random_digits_CS}",
                    f"AMIDEWINx64.EXE /CSH {random_digits_CSH}",
                    f"AMIDEWINx64.EXE /PSN {random_digits_PSN}",
                    f"AMIDEWINx64.EXE /PBS {random_digits_PBS}",
                    "AMIDEWINx64.EXE /ALL post_spoof.txt",
                ]

                # Create and run the batch file
                Spoofer.DMISpoofer.create_and_run_batch_file(path_to_directory, commands_to_run)

                # Compare the pre and post spoof files and log the differences
                pre_spoof_file = os.path.join(path_to_directory, "pre_spoof.txt")
                post_spoof_file = os.path.join(path_to_directory, "post_spoof.txt")
                
                Spoofer.DMISpoofer.compare_files(pre_spoof_file, post_spoof_file)

                # Remove 'R    Done' from the comparison file
                Spoofer.DMISpoofer.remove_r_done(pre_spoof_file)
                Spoofer.DMISpoofer.remove_r_done(post_spoof_file)

                # Delete pre and post spoof files
                os.remove(pre_spoof_file)
                os.remove(post_spoof_file)
            else:
                Spoofer.DMISpoofer.log_message(f"{file_to_find} not found.")


    class AutoRestart:
        @staticmethod
        def spoof():
            print("Il sistema si riavvierà in 5 secondi...")
            time.sleep(5)
            Spoofer.AutoRestart._perform_reboot()

        @staticmethod
        def _perform_reboot():
            os.system("shutdown /r /t 0")


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


