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
    if Spoofer.BuildGUID.spoof():
        messagebox.showinfo("Successo", "Build GUID modificato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica del Build GUID")

def spoof_registered_organization():
    if Spoofer.RegisteredOrganization.spoof():
        messagebox.showinfo("Successo", "Registered Organization modificato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica del Registered Organization")

def spoof_machine_id():
    if Spoofer.MachineId.spoof():
        messagebox.showinfo("Successo", "Machine ID modificato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica del Machine ID")

def spoof_hardware_guid():
    if Spoofer.HardwareGUID.spoof():
        messagebox.showinfo("Successo", "Hardware GUID modificato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica dell'Hardware GUID")

def spoof_machine_guid():
    if Spoofer.MachineGUID.spoof():
        messagebox.showinfo("Successo", "Machine GUID modificato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica del Machine GUID")

def spoof_efi_variables():
    if Spoofer.EFIVariables.spoof():
        messagebox.showinfo("Successo", "EFI Variables modificate con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica delle EFI Variables")

def spoof_system_info():
    if Spoofer.SystemInfo.spoof():
        messagebox.showinfo("Successo", "Informazioni di sistema modificate con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica delle informazioni di sistema")

def spoof_product_id():
    if Spoofer.ProductId.spoof():
        messagebox.showinfo("Successo", "Product ID modificato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica del Product ID")

def spoof_os_install_date():
    if Spoofer.OSInstallDate.spoof():
        messagebox.showinfo("Successo", "Install Date modificata con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica dell'Install Date")

def spoof_installation_id():
    if Spoofer.InstallationID.spoof():
        messagebox.showinfo("Successo", "Installation ID modificato con successo")
    else:
        messagebox.showerror("Errore", "Errore durante la modifica dell'Installation ID")

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

def auto_restart():
    messagebox.showinfo("Riavvio", "Il sistema si riavvierà in 5 secondi...")
    time.sleep(5)
    Spoofer.AutoRestart.spoof()

# Finestra principale
root = tk.Tk()
root.title("Spoofer GUI")

# Creazione di una griglia per disporre i pulsanti in 4 colonne
button_list = [
    ("Spoof Build GUID", spoof_build_guid),
    ("Spoof Registered Organization", spoof_registered_organization),
    ("Spoof Machine ID", spoof_machine_id),
    ("Spoof Hardware GUID", spoof_hardware_guid),
    ("Spoof Machine GUID", spoof_machine_guid),
    ("Spoof EFI Variables", spoof_efi_variables),
    ("Spoof System Info", spoof_system_info),
    ("Spoof Product ID", spoof_product_id),
    ("Spoof OS Install Date", spoof_os_install_date),
    ("Spoof Installation ID", spoof_installation_id),
    ("Spoof MAC Address", spoof_mac_address),
    ("Spoof Display EDID", spoof_display_edid),
    ("Spoof Disk Serial Number", spoof_disk_serial),
    ("Spoof Disk GUID", spoof_disk_guid),
    ("Rename Disk Label", spoof_rename_disk),
    ("Spoof NVIDIA ClientUUID", spoof_nvidia_client_uuid),
    ("Spoof NVIDIA Chipset Match ID", spoof_nvidia_chipset_id),
    ("Spoof DMI Information", spoof_dmi),
    ("Rename Computer/User", rename_computer_user),
    ("Auto Restart", auto_restart)
]

# Posizionamento dei pulsanti nella griglia (4 colonne)
for i, (text, command) in enumerate(button_list):
    row = i // 4
    column = i % 4
    tk.Button(root, text=text, command=lambda cmd=command: run_in_background(cmd)).grid(row=row, column=column, padx=10, pady=10, sticky="ew")

# Avvio dell'interfaccia grafica
root.mainloop()

