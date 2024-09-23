**SpectreSafe**

This script provides comprehensive functionality to spoof various hardware and software identifiers on a Windows machine, enhancing user privacy and security. It modifies system registry entries, executes system commands, and manipulates data to alter machine. However, it does not change the serial numbers of SSDs, GPU UUIDs, or RAM serial numbers.

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

- **[NEW] Custom MAC Address Generation: For "TAP-NordVPN Windows Provider V9"

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
