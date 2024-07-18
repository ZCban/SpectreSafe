import winreg
import subprocess

def disable_privacy_settings():
    disable_ad_tracking()
    disable_activity_history()
    disable_location_tracking()
    disable_diagnostics_feedback()
    disable_cortana()
    disable_typing_data_collection()
    disable_voice_data_collection()
    disable_feedback_notifications()
    disable_edge_privacy_settings()

def disable_ad_tracking():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\AdvertisingInfo', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'Enabled', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print("Pubblicità personalizzata disattivata.")
    except Exception as e:
        print(f"Errore durante la disattivazione della pubblicità personalizzata: {e}")

def disable_activity_history():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows\System', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'PublishUserActivities', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print("Cronologia delle attività disattivata.")
    except Exception as e:
        print(f"Errore durante la disattivazione della cronologia delle attività: {e}")

def disable_location_tracking():
    try:
        subprocess.run(['powershell', '-Command', 'Set-Service -Name lfsvc -StartupType Disabled'], check=True)
        subprocess.run(['powershell', '-Command', 'Stop-Service -Name lfsvc'], check=True)
        print("Tracciamento della posizione disattivato.")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante la disattivazione del tracciamento della posizione: {e}")

def disable_diagnostics_feedback():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows\DataCollection', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'AllowTelemetry', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print("Diagnostica e dati di feedback disattivati.")
    except Exception as e:
        print(f"Errore durante la disattivazione della diagnostica e dei dati di feedback: {e}")

def disable_cortana():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows\Windows Search', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'AllowCortana', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print("Cortana disattivata.")
    except Exception as e:
        print(f"Errore durante la disattivazione di Cortana: {e}")

def disable_typing_data_collection():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\InputPersonalization', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'RestrictImplicitTextCollection', 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(key, 'RestrictImplicitInkCollection', 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
        print("Raccolta dati sulla digitazione disattivata.")
    except Exception as e:
        print(f"Errore durante la disattivazione della raccolta dati sulla digitazione: {e}")

def disable_voice_data_collection():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows\Speech', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'AllowInputPersonalization', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print("Raccolta dati sulla voce disattivata.")
    except FileNotFoundError:
        print("La chiave di registro per la raccolta dati sulla voce non è stata trovata.")

def disable_feedback_notifications():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Siuf\Rules', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'NumberOfSIUFInPeriod', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Siuf\Rules', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'PeriodInNanoSeconds', 0, winreg.REG_QWORD, 0)
        winreg.CloseKey(key)
        print("Notifiche di feedback disattivate.")
    except Exception as e:
        print(f"Errore durante la disattivazione delle notifiche di feedback: {e}")

def disable_edge_privacy_settings():
    try:
        subprocess.run(['powershell', '-Command', 'Set-ItemProperty -Path "HKCU:\\Software\\Policies\\Microsoft\\MicrosoftEdge\\Main" -Name "DoNotTrack" -Value 1'], check=True)
        subprocess.run(['powershell', '-Command', 'Set-ItemProperty -Path "HKCU:\\Software\\Policies\\Microsoft\\Edge\\Privacy" -Name "SendDoNotTrackHeader" -Value 1'], check=True)
        print("Impostazioni di privacy di Microsoft Edge configurate.")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante la configurazione delle impostazioni di privacy di Microsoft Edge: {e}")



disable_privacy_settings()
