**SpectreSafe**

This script provides comprehensive functionality to spoof various hardware and software identifiers on a Windows machine, enhancing user privacy and security. It modifies system registry entries, executes system commands, and manipulates data to alter machine. However, it does not change the serial numbers of SSDs, GPU UUIDs, or RAM serial numbers.

Additionally, the script provides powerful system maintenance features, including extensive system cleaning, service management, and removal of non-connected devices. These capabilities collectively improve system performance and safeguard user privacy.

## Features

**PowerShell Script Unlocking**: Enables the execution of PowerShell scripts by changing the execution policy.

**Auto-Restart**: Restarts the system automatically after script execution is complete.

**Machine ID Spoofing**: Changes the machine ID in the registry.

**Hardware GUID Spoofing**: Modifies the hardware profile GUID.

**Machine GUID Spoofing**: Updates the machine GUID.

**EFI Variables Spoofing**: Changes EFI variables in the registry.

**System Information Spoofing**: Modifies BIOS release date, BIOS version, and computer hardware ID.

**Extended System Information Spoofing**: Spoofs various system and BIOS information.

**Product ID Spoofing**: Changes the Windows Product ID.

**Installation ID Spoofing**: Modifies the installation ID in the registry.

**NVIDIA Settings Spoofing**: Changes NVIDIA ClientUUID and ChipsetMatchID.

**Disk Volume Label Spoofing**: Changes the volume label of available drives.

**Disk Unique ID Spoofing**: Changes the unique ID of non-system disks.

**Volume Serial Number Spoofing**: Modifies the volume serial numbers of available drives.

**MAC Address Spoofing**: Changes the MAC address of network adapters.

**Display EDID Spoofing**: Modifies EDID data for displays.

**DMI Information Spoofing**: Changes DMI information using the AMIDEWINx64 tool (requires AMIDEWINx64.EXE to be present on the C: drive). This includes:
- **System Serial Number Spoofing**: Changes the system serial number.
- **Baseboard Serial Number Spoofing**: Modifies the baseboard serial number.
- **Baseboard Asset Tag Spoofing**: Changes the baseboard asset tag.
- **Chassis Serial Number Spoofing**: Modifies the chassis serial number.
- **Chassis Asset Tag Spoofing**: Changes the chassis asset tag.
- **Processor Serial Number Spoofing**: Alters the processor serial number.
- **Processor Asset Tag Spoofing**: Changes the processor asset tag.
- **Before and After Report Generation**: Generates reports before and after spoofing to verify changes.

**Service Management**: Sets specified services to manual start and removes non-connected devices. This is managed by the ServiceManager class, which includes:

- **Setting Services to Manual Start**: The script sets the startup type of various services to manual. These services include AdobeARMservice, DropboxUpdate, Steam Client Service, and many others. The set_services_to_manual method iterates through a predefined list of services, changing their startup type to manual.
- **Removing Non-Connected Devices**: The script uses PowerShell to list all PnP devices and removes those that are not currently connected. The remove_non_connected_devices method retrieves the list of devices and removes the non-connected ones using the pnputil command.

**System Cleaning**: Cleans system files and browser data, including:

- **Clean Temporary System Files**: Uses the cleanmgr utility to remove temporary files and deletes temporary files from the system's temp folder.
- **Clean Windows Log Files**: Deletes log files from the Windows logs directory and cleans logs from the Panther directory.
- **Clean DNS Cache**: Flushes the DNS cache to remove any old or invalid DNS entries.
- **Reset DNS Client and TCP/IP Settings**: Deletes the ARP cache, resets Winsock settings, and resets IP configurations.
- **Clean Windows Error Reporting**: Deletes Windows error reporting minidumps and clears Windows event logs.
- **Remove Obsolete Installation Files**: Uses the Dism utility to clean up the component store and obsolete Windows update files.
- **Clean User Downloads Folder**: Deletes files from the user's Downloads folder.
- **Clean Recycle Bin**: Empties the Recycle Bin.
- **Clean System Restore Files**: Deletes all system restore points.
- **Optimize Boot Configuration**: Adjusts boot configuration to ignore all boot failures.
- **Clear Scheduled Tasks**: Deletes all scheduled tasks.
- **Reset Firewall Rules**: Resets Windows Firewall rules to default settings.
- **Clear USB Device History**: Deletes the registry entries for USB devices.
- **Clear Browser Data**: Deletes cache, cookies, history, session data, and download metadata for installed browsers (Google Chrome, Mozilla Firefox, Microsoft Edge, Opera, Brave).
- **Disable automatic paging**
- **Disable ReadyBoost and Memory Compression**
- **Disable Notification**
- **Disable UAC**

## Installation

1. **Clone the repository:**
   
bash
   git clone <repository_url>
   cd <repository_directory>

## Install necessary Python libraries:
Ensure you have ctypes, subprocess, uuid, winreg, os, random, string, datetime, re, time, logging, and json available in your Python environment.

## Run the script with administrative privileges:
Open a command prompt as an administrator and execute,The script will attempt to perform all the spoofing operations and log the changes to spoofer_log.txt.


## Disclaimer
This script is intended for educational purposes only. Misuse of this script may result in system instability . Use at your own risk.
