import os
import subprocess
import ctypes
import json
from ctypes import wintypes

class ServiceManager:
    @staticmethod
    def is_admin():
        """Check if the script is running with administrative privileges."""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    @staticmethod
    def run_command_as_admin(command, description):
        """Run a command with administrative privileges."""
        if ServiceManager.is_admin():
            try:
                print(f'Executing: {description}')
                result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
                print(f"Output: {result.stdout}")
            except subprocess.CalledProcessError as e:
                print(f"Error: {e.stderr}")
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", f'"{os.path.abspath(__file__)}" {command}', None, 1)

    @staticmethod
    def get_pnp_devices_powershell():
        """Get PnP devices using PowerShell."""
        command = "powershell -Command \"Get-PnpDevice | Select-Object -Property FriendlyName, Present, InstanceId | ConvertTo-Json\""
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        devices = json.loads(result.stdout)
        return devices

    @staticmethod
    def remove_device(instance_id):
        """Remove a device using its instance ID with pnputil command."""
        result = subprocess.run(["pnputil", "/remove-device", instance_id], capture_output=True, text=True)
        return result.stdout

    @staticmethod
    def remove_non_connected_devices():
        """Remove non-connected devices."""
        # Get all devices using PowerShell
        devices = ServiceManager.get_pnp_devices_powershell()

        # Filter out non-connected devices
        non_connected_devices = [d for d in devices if not d["Present"]]

        print("\nElenco dei dispositivi Non collegati:")
        if non_connected_devices:
            for device in non_connected_devices:
                print(f"{device['FriendlyName']} - Non collegato")

            print("\nInizio rimozione dei dispositivi non collegati...")
            for device in non_connected_devices:
                print(f"Rimozione del dispositivo: {device['FriendlyName']}")
                output = ServiceManager.remove_device(device["InstanceId"])
                print(output)
            print("Rimozione completata.")
        else:
            print("Nessun dispositivo non collegato trovato.")

        # Remove old log file from desktop if it exists
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        log_file = os.path.join(desktop_path, "OldDeviceLog.txt")
        if os.path.exists(log_file):
            os.remove(log_file)

    @staticmethod
    def clean_system_files():
        """Perform various system cleaning tasks."""
        # Clean temporary system files
        ServiceManager.run_command_as_admin("cleanmgr /sagerun:1", "Clean temporary system files")

        # Clean Windows temporary files
        ServiceManager.run_command_as_admin("del /q /f /s %temp%\\*", "Clean Windows temporary files")

        # Clean Windows log files
        ServiceManager.run_command_as_admin("del /q /f /s %systemroot%\\Logs\\*", "Clean Windows log files")
        ServiceManager.run_command_as_admin("del /q /f /s %systemroot%\\Panther\\*", "Clean Windows Panther logs")

        # Clean DNS cache
        ServiceManager.run_command_as_admin("ipconfig /flushdns", "Flush DNS cache")

        # Reset DNS client
        ServiceManager.run_command_as_admin("netsh interface ip delete arpcache", "Delete ARP cache")
        ServiceManager.run_command_as_admin("netsh winsock reset", "Reset Winsock")

        # Reset TCP/IP settings
        ServiceManager.run_command_as_admin("netsh winsock reset", "Reset Winsock again")
        ServiceManager.run_command_as_admin("netsh int ip reset", "Reset IP")

        # Clean Windows Error Reporting
        ServiceManager.run_command_as_admin("del /q /f /s %systemroot%\\Minidump\\*", "Clean Windows Minidump")
        ServiceManager.run_command_as_admin("WEvtUtil cl Application", "Clear Windows Event Logs - Application")

        # Remove obsolete installation files
        ServiceManager.run_command_as_admin("Dism.exe /online /Cleanup-Image /StartComponentCleanup /ResetBase", "Remove obsolete installation files")

        # Clean Downloads folder
        ServiceManager.run_command_as_admin("del /q /f /s %userprofile%\\Downloads\\*", "Clean Downloads folder")

        # Clean Recycle Bin
        ServiceManager.run_command_as_admin("rd /s /q %systemdrive%\\$Recycle.bin", "Clean Recycle Bin")

        # Clean System Restore files
        ServiceManager.run_command_as_admin("vssadmin Delete Shadows /All /Quiet", "Clean System Restore files")

        # Clean obsolete Windows Update files
        ServiceManager.run_command_as_admin("Dism.exe /online /Cleanup-Image /SPSuperseded", "Clean obsolete Windows Update files")

        # Clean Windows Component Store
        ServiceManager.run_command_as_admin("Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore", "Analyze Component Store")

        # Clear Windows Event Logs
        ServiceManager.run_command_as_admin("for /F \"tokens=*\" %1 in ('wevtutil.exe el') DO wevtutil.exe cl \"%1\"", "Clear Windows Event Logs")

        # Clear Prefetch Files
        ServiceManager.run_command_as_admin("del /q /f /s C:\\Windows\\Prefetch\\*", "Clear Prefetch files")

        # Disable Delivery Optimization
        ServiceManager.run_command_as_admin("net stop dosvc", "Stop Delivery Optimization service")

        # Clear Thumbnail Cache
        ServiceManager.run_command_as_admin("del /q /f /s %userprofile%\\AppData\\Local\\Microsoft\\Windows\\Explorer\\thumbcache_*", "Clear Thumbnail cache")

        # Clear Windows Update Cache
        ServiceManager.run_command_as_admin("net stop wuauserv && del /q /f /s %systemroot%\\SoftwareDistribution\\* && net start wuauserv", "Clear Windows Update cache")

        # Disable Indexing
        ServiceManager.run_command_as_admin("sc config wsearch start=disabled && net stop wsearch", "Disable Indexing service")

        # Optimize Boot Configuration
        ServiceManager.run_command_as_admin("bcdedit /set {current} bootstatuspolicy ignoreallfailures", "Optimize Boot Configuration")

        # Clear Scheduled Tasks
        ServiceManager.run_command_as_admin("schtasks /Delete /TN * /F", "Clear scheduled tasks")

        # Reset Firewall Rules
        ServiceManager.run_command_as_admin("netsh advfirewall reset", "Reset firewall rules")

        # Clear USB Device History
        ServiceManager.run_command_as_admin('reg delete "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Enum\\USBSTOR" /f', "Clear USB device history")

        # Disable automatic paging file management for all drives
        ServiceManager.run_command_as_admin('wmic computersystem set AutomaticManagedPagefile=False', "Disable automatic paging for all drives")

        # Disable ReadyBoost and Memory Compression
        commands = ['reg add "HKLM\\SYSTEM\\ControlSet001\\Control\\Class\\{71a27cdd-812a-11d0-bec7-08002be2092f}" /v "LowerFilters" /t REG_MULTI_SZ /d "fvevol\\0iorate" /f',
                    'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\rdyboost" /v "Start" /t REG_DWORD /d "4" /f',
                    'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SysMain" /v "Start" /t REG_DWORD /d "4" /f',
                    'reg add "HKLM\\SYSTEM\\ControlSet001\\Control\\Session Manager\\Memory Management\\PrefetchParameters" /v "EnablePrefetcher" /t REG_DWORD /d "0" /f',
                    'reg add "HKLM\\SYSTEM\\ControlSet001\\Control\\Session Manager\\Memory Management\\PrefetchParameters" /v "EnableSuperfetch" /t REG_DWORD /d "0" /f',
                    'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\EMDMgmt" /v "GroupPolicyDisallowCaches" /t REG_DWORD /d "1" /f',
                    'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\EMDMgmt" /v "AllowNewCachesByDefault" /t REG_DWORD /d "0" /f',
                    'PowerShell -NonInteractive -NoLogo -NoProfile -Command "Disable-MMAgent -mc"',
                    'reg add "HKLM\\SYSTEM\\ControlSet001\\Control\\Session Manager\\Memory Management\\PrefetchParameters" /v "isMemoryCompressionEnabled" /t REG_DWORD /d "0" /f']
        for command in commands:
            ServiceManager.run_command_as_admin(command, "Disable ReadyBoost and Memory Compression")



remove_non_connected_devices()
clean_system_files()
