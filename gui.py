import tkinter as tk
from tkinter import messagebox
import threading
import time

# Classe Spoofer già esistente (presumibilmente importata dal tuo codice originale)
from SpectreSafe import Spoofer  # Assicurati che il file Spoofer.py sia nella stessa directory o aggiornare il percorso

# Funzione per eseguire in background con threading
def run_in_background(func):
    thread = threading.Thread(target=func)
    thread.start()

# Funzioni per eseguire le funzionalità dello Spoofer
def spoof_build_guid():
    return Spoofer.BuildGUID.spoof()

def spoof_registered_organization():
    return Spoofer.RegisteredOrganization.spoof()

def spoof_machine_id():
    return Spoofer.MachineId.spoof()

def spoof_hardware_guid():
    return Spoofer.HardwareGUID.spoof()

def spoof_machine_guid():
    return Spoofer.MachineGUID.spoof()

def spoof_efi_variables():
    return Spoofer.EFIVariables.spoof()

def spoof_system_info():
    return Spoofer.SystemInfo.spoof()

def spoof_product_id():
    return Spoofer.ProductId.spoof()

def spoof_os_install_date():
    return Spoofer.OSInstallDate.spoof()

def spoof_installation_id():
    return Spoofer.InstallationID.spoof()

# Nuova funzione che combina tutte le funzioni di spoofing elencate
def spoof_guid_related():
    if (spoof_build_guid() and
        spoof_registered_organization() and
        spoof_machine_id() and
        spoof_hardware_guid() and
        spoof_machine_guid() and
        spoof_efi_variables() and
        spoof_system_info() and
        spoof_product_id() and
        spoof_os_install_date() and
        spoof_installation_id()):
        messagebox.showinfo("Successo", "Tutti i GUID e le informazioni correlate sono stati modificati con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica di uno o più GUID o informazioni correlate")

# Funzioni esistenti per le altre operazioni di spoofing
def spoof_mac_address():
    if Spoofer.MacAddressSpoofer.spoof():
        messagebox.showinfo("Successo", "MAC Address modificato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica del MAC Address")

def spoof_display_edid():
    if Spoofer.spoof_display_edid():
        messagebox.showinfo("Successo", "Display EDID modificato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica del Display EDID")

def spoof_disk_serial():
    if Spoofer.VolumeSerialNumberSpoofer.spoof_volume_serial_numbers():
        messagebox.showinfo("Successo", "Volume Serial Number modificato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica del Volume Serial Number")

def spoof_disk_guid():
    if Spoofer.DiskSpoofer.list_disks_and_spoof_unique_ids():
        messagebox.showinfo("Successo", "Disk GUID modificato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica del Disk GUID")

def spoof_rename_disk():
    if Spoofer.RenameDiskSpoofer.spoof():
        messagebox.showinfo("Successo", "Disk Label rinominato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la rinominazione del Disk Label")

def spoof_nvidia_client_uuid():
    if Spoofer.NvidiaSettings.modify_registry_ClientUUID():
        messagebox.showinfo("Successo", "NVIDIA ClientUUID modificato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica del NVIDIA ClientUUID")

def spoof_nvidia_chipset_id():
    if Spoofer.NvidiaSettings.modify_registry_ChipsetMatchID():
        messagebox.showinfo("Successo", "NVIDIA Chipset Match ID modificato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica del NVIDIA Chipset Match ID")

def spoof_dmi():
    if Spoofer.DMISpoofer.spoof_dmi():
        messagebox.showinfo("Successo", "DMI informazioni modificate con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica delle informazioni DMI")

def rename_computer_user():
    if Spoofer.ComputerUserRenamer.spoof():
        messagebox.showinfo("Successo", "Computer/User rinominato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la rinominazione del Computer/User")

def remove_non_connected_devices():
    if Spoofer.PnpRemover.remove_non_connected_devices():
        messagebox.showinfo("Successo", "rimozione vecchi dispositivi con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la rimozione vecchi dispositivi")

def auto_restart():
    messagebox.showinfo("Riavvio", "Il sistema si riavvierà in 5 secondi...")
    Spoofer.AutoRestart.spoof()

# Funzione per eseguire tutte le operazioni di spoof (eccetto le ultime due)
def spoof_all():
    Spoofer.BuildGUID.spoof()
    Spoofer.RegisteredOrganization.spoof()
    Spoofer.MachineId.spoof()
    Spoofer.HardwareGUID.spoof()
    Spoofer.MachineGUID.spoof()
    Spoofer.EFIVariables.spoof()
    Spoofer.SystemInfo.spoof()
    Spoofer.ProductId.spoof()
    Spoofer.OSInstallDate.spoof()
    Spoofer.InstallationID.spoof()
    Spoofer.MacAddressSpoofer.spoof()
    print('mac spoofed')
    Spoofer.spoof_display_edid()
    print('edid spoofed')
    Spoofer.VolumeSerialNumberSpoofer.spoof_volume_serial_numbers()
    print('volume disk spoofed')
    Spoofer.DiskSpoofer.list_disks_and_spoof_unique_ids()
    print('guid disk spoofed')
    Spoofer.RenameDiskSpoofer.spoof()
    print('rename disk spoofed')
    #Spoofer.NvidiaSettings.modify_registry_ClientUUID()
    #Spoofer.NvidiaSettings.modify_registry_ChipsetMatchID()
    Spoofer.DMISpoofer.spoof_dmi()
    print('dmi spoofed')
    Spoofer.PnpRemover.remove_non_connected_devices()
    print('removed old device')
    Spoofer.ComputerUserRenamer.spoof()
    print('rename pc and user  spoofed')
    Spoofer.AutoRestart.spoof()


# Finestra principale
root = tk.Tk()
root.title("Spoofer GUI")

# Creazione di una griglia per disporre i pulsanti in 4 colonne
button_list = [
    ("Spoof All", spoof_all),  # Aggiunto bottone per eseguire tutte le funzioni
    ("Spoof GUID & Regedit", spoof_guid_related),  # Bottone combinato per tutte le funzioni GUID
    ("Spoof MAC Address", spoof_mac_address),
    ("Spoof Display EDID", spoof_display_edid),
    ("Spoof Disk Vol.Serial Number", spoof_disk_serial),
    ("Spoof Disk GUID", spoof_disk_guid),
    ("Rename Disk Label", spoof_rename_disk),
    #("Spoof NVIDIA ClientUUID", spoof_nvidia_client_uuid),
    #("Spoof NVIDIA Chipset Match ID", spoof_nvidia_chipset_id),
    ("Spoof DMI Information", spoof_dmi),
    ("Rename Computer/User", rename_computer_user),
    ("Remove old device", remove_non_connected_devices),
    ("Auto Restart", auto_restart)
]

# Posizionamento dei pulsanti nella griglia (4 colonne)
for i, (text, command) in enumerate(button_list):
    row = i // 4
    column = i % 4
    tk.Button(root, text=text, command=lambda cmd=command: run_in_background(cmd)).grid(row=row, column=column, padx=10, pady=10, sticky="ew")

# Avvio dell'interfaccia grafica
root.mainloop()


