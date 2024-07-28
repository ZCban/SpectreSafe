import winreg
import ctypes
import os
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_command_as_admin(command):
    if is_admin():
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            print(f"Output: {result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr}")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", f'"{os.path.abspath(__file__)}" {command}', None, 1)

def set_registry_value_current_user(path, name, value, reg_type=winreg.REG_SZ):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, name, 0, reg_type, value)
        winreg.CloseKey(key)
        print(f"La chiave '{name}' è stata impostata a {value}.")
    except Exception as e:
        print(f"Errore durante la modifica del registro: {e}")

def set_registry_value_local_machine(path, name, value, reg_type=winreg.REG_SZ):
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, name, 0, reg_type, value)
        winreg.CloseKey(key)
        print(f"La chiave '{name}' è stata impostata a {value}.")
    except Exception as e:
        print(f"Errore durante la modifica del registro: {e}")

def device_input_dalay():
    # Imposta i valori desiderati
    set_registry_value_current_user(r"Control Panel\Desktop", "MenuShowDelay", "5")
    set_registry_value_current_user(r"Control Panel\Mouse", "MouseHoverTime", "1")
    set_registry_value_current_user(r"Control Panel\Mouse", "MouseSensitivity", "9")
    set_registry_value_current_user(r"Control Panel\Mouse", "MouseThreshold1", "0")
    set_registry_value_current_user(r"Control Panel\Mouse", "MouseThreshold2","0")
    set_registry_value_current_user(r"Control Panel\Mouse", "MouseSpeed", "0")
    set_registry_value_current_user(r"Control Panel\Mouse", "DoubleClickSpeed", "200")
    set_registry_value_current_user(r"Control Panel\Keyboard", "KeyboardSpeed", "31")
    set_registry_value_current_user(r"Control Panel\Keyboard", "KeyboardDelay", "0")
    set_registry_value_current_user(r"Control Panel\Desktop", "LowLevelHooksTimeout", "10")
    set_registry_value_current_user(r"Control Panel\Desktop", "ForegroundLockTimeout", "0")
    set_registry_value_current_user(r"Control Panel\Desktop", "WaitToKillAppTimeout", "2000")
    set_registry_value_current_user(r"Control Panel\Desktop", "HungAppTimeout", "1000")

def improve_screencapture():
    # Imposta i valori desiderati
    set_registry_value_current_user(r"Software\Microsoft\Avalon.Graphics", "DisableHWAcceleration", "1")
    set_registry_value_current_user(r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects", "VisualFXSetting", "2")
    set_registry_value_current_user(r"Software\Microsoft\Windows\DWM", "Composition", "0")
    set_registry_value_local_machine(r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management", "LargeSystemCache", 1, winreg.REG_DWORD)

def improve_ping():
    set_registry_value_local_machine(r"SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters", "IRPStackSize", 32, winreg.REG_DWORD)
    set_registry_value_local_machine(r"SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters", "SizReqBuf", 17424, winreg.REG_DWORD)  # 17 kilobyte
    set_registry_value_local_machine(r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "DefaultTTL", 64, winreg.REG_DWORD)
    set_registry_value_local_machine(r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "Tcp1323Opts", 1, winreg.REG_DWORD)
    set_registry_value_local_machine(r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "MaxFreeTcbs", 65536, winreg.REG_DWORD)
    set_registry_value_local_machine(r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "MaxUserPort", 65534, winreg.REG_DWORD)
    set_registry_value_local_machine(r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "GlobalMaxTcpWindowSize", 65535, winreg.REG_DWORD)
    set_registry_value_local_machine(r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "TcpNoDelay", 1, winreg.REG_DWORD)
    set_registry_value_local_machine(r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "TcpAckFrequency", 1, winreg.REG_DWORD)

def optimize_disk():
    set_registry_value_local_machine(r"SYSTEM\CurrentControlSet\Control\FileSystem", "NtfsDisableLastAccessUpdate", 1, winreg.REG_DWORD)
    set_registry_value_local_machine(r"SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters", "DirectoryCacheLifetime", 0, winreg.REG_DWORD)
    set_registry_value_local_machine(r"SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters", "FileInfoCacheLifetime", 0, winreg.REG_DWORD)
    set_registry_value_local_machine(r"SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters", "FileNotFoundCacheLifetime", 0, winreg.REG_DWORD)

def enable_windows_defender():
    commands = [
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\MsSecFlt" /v "Start" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SecurityHealthService" /v "Start" /t REG_DWORD /d "3" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\Sense" /v "Start" /t REG_DWORD /d "3" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdBoot" /v "Start" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdFilter" /v "Start" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdNisDrv" /v "Start" /t REG_DWORD /d "3" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdNisSvc" /v "Start" /t REG_DWORD /d "3" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WinDefend" /v "Start" /t REG_DWORD /d "2" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /v "SecurityHealth" /t REG_EXPAND_SZ /d "%systemroot%\\system32\\SecurityHealthSystray.exe" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SgrmAgent" /v "Start" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SgrmBroker" /v "Start" /t REG_DWORD /d "2" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\webthreatdefsvc" /v "Start" /t REG_DWORD /d "3" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\webthreatdefusersvc" /v "Start" /t REG_DWORD /d "2" /f',
        'reg delete "HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\smartscreen.exe" /f',
        'reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Associations" /f',
        'reg delete "HKLM\\Software\\Policies\\Microsoft\\Windows Defender\\SmartScreen" /f',
        'reg delete "HKLM\\Software\\Policies\\Microsoft\\Windows Defender\\Signature Updates" /f'
    ]
    for command in commands:
        run_command_as_admin(command)
    print("Windows Defender has been enabled successfully! Please restart your PC.")

def disable_windows_defender():
    commands = [
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\MsSecFlt" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SecurityHealthService" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\Sense" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdBoot" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdFilter" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdNisDrv" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WdNisSvc" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\WinDefend" /v "Start" /t REG_DWORD /d "4" /f',
        'reg delete "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /v "SecurityHealth" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SgrmAgent" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\SgrmBroker" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\webthreatdefsvc" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\ControlSet001\\Services\\webthreatdefusersvc" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\smartscreen.exe" /v "Debugger" /t REG_SZ /d "%%windir%%\\System32\\taskkill.exe" /f',
        'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Associations" /v "DefaultFileTypeRisk" /t REG_DWORD /d "1808" /f',
        'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Attachments" /v "SaveZoneInformation" /t REG_DWORD /d "1" /f',
        'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Associations" /v "LowRiskFileTypes" /t REG_SZ /d ".avi;.bat;.com;.cmd;.exe;.htm;.html;.lnk;.mpg;.mpeg;.mov;.mp3;.msi;.m3u;.rar;.reg;.txt;.vbs;.wav;.zip;" /f',
        'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Associations" /v "ModRiskFileTypes" /t REG_SZ /d ".bat;.exe;.reg;.vbs;.chm;.msi;.js;.cmd" /f',
        'reg add "HKLM\\Software\\Policies\\Microsoft\\Windows Defender\\SmartScreen" /v "ConfigureAppInstallControlEnabled" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\Software\\Policies\\Microsoft\\Windows Defender\\SmartScreen" /v "ConfigureAppInstallControl" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\Software\\Policies\\Microsoft\\Windows Defender\\SmartScreen" /v "EnableSmartScreen" /t REG_DWORD /d "0" /f',
        'reg add "HKCU\\Software\\Policies\\Microsoft\\MicrosoftEdge\\PhishingFilter" /v "EnabledV9" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\Software\\Policies\\Microsoft\\MicrosoftEdge\\PhishingFilter" /v "EnabledV9" /t REG_DWORD /d "0" /f'
    ]
    for command in commands:
        run_command_as_admin(command)
    print("Windows Defender has been disabled successfully! Please restart your PC.")

def disable_firewall():
    commands = [
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile" /v "EnableFirewall" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\DomainProfile" /v "EnableFirewall" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\PublicProfile" /v "EnableFirewall" /t REG_DWORD /d "0" /f'
    ]
    for command in commands:
        run_command_as_admin(command)
    print("Windows Firewall has been disabled successfully!")

def disable_notifications():
    commands = [
        'reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings" /v "NOC_GLOBAL_SETTING_ALLOW_TOASTS_ABOVE_LOCK" /t REG_DWORD /d "0" /f',
        'reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings" /v "NOC_GLOBAL_SETTING_ALLOW_CRITICAL_TOASTS_ABOVE_LOCK" /t REG_DWORD /d "0" /f',
        'reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings" /v "NOC_GLOBAL_SETTING_TOASTS_ENABLED" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer" /v "DisableNotificationCenter" /t REG_DWORD /d "1" /f',
        'reg add "HKCU\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer" /v "DisableNotificationCenter" /t REG_DWORD /d "1" /f',
        'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /v "ToastEnabled" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /v "ToastEnabled" /t REG_DWORD /d "0" /f',
        'reg add "HKCU\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /v "NoToastApplicationNotification" /t REG_DWORD /d "1" /f',
        'reg add "HKCU\\Software\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /v "NoTileApplicationNotification" /t REG_DWORD /d "1" /f',
        'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer" /v "IsNotificationsEnabled" /t REG_DWORD /d "0" /f',
        #'taskkill /im explorer.exe /f',
        #'start explorer.exe'
    ]
    for command in commands:
        run_command_as_admin(command)
    print("Notifications have been disabled successfully.")

def disable_onedrive():
    commands = [
        'taskkill /f /im OneDrive.exe',
        'REG ADD "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\OneDrive" /v "DisableFileSyncNGSC" /t REG_DWORD /d 1 /f',
        'REG ADD "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\OneDrive" /v "DisableFileSync" /t REG_DWORD /d 1 /f',
        'REG ADD "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v "ShowSyncProviderNotifications" /t REG_DWORD /d 0 /f'
    ]
    for command in commands:
        run_command_as_admin(command)
    print("OneDrive è stato disabilitato con successo.")

def disable_uac():
    commands = [
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "EnableVirtualization" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "EnableInstallerDetection" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "PromptOnSecureDesktop" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "EnableLUA" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "EnableSecureUIAPaths" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "ConsentPromptBehaviorAdmin" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "ValidateAdminCodeSignatures" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "EnableUIADesktopToggle" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "ConsentPromptBehaviorUser" /t REG_DWORD /d "0" /f',
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "FilterAdministratorToken" /t REG_DWORD /d "0" /f'
    ]
    for command in commands:
        run_command_as_admin(command)
    print("UAC has been disabled successfully. Please restart your PC.")

def enable_show_hidden_files():
    try:
        # Abilita la visualizzazione di file e cartelle nascosti
        subprocess.run('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden /t REG_DWORD /d 1 /f', shell=True, check=True)
        print("La visualizzazione di file e cartelle nascosti è stata abilitata con successo.")
    except subprocess.CalledProcessError as e:
        print("Si è verificato un errore durante l'abilitazione della visualizzazione di file e cartelle nascosti:", e)
        print("Fallito.")

def enable_auto_date_time():
    try:
        # Imposta la sincronizzazione automatica della data e dell'ora tramite il Registro di sistema
        subprocess.run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\W32Time\\TimeProviders\\NtpClient" /v "Enabled" /t REG_DWORD /d 1 /f', shell=True)
        subprocess.run('w32tm /config /update', shell=True)
        print("Impostazione della data e dell'ora automatiche abilitata con successo.")
    except Exception as e:
        print("Errore durante l'abilitazione della data e dell'ora automatiche:", str(e))

def disable_recent_files():
    try:
        # Disables recent files feature
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "NoRecentDocsHistory", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
        print("Recent files feature disabled successfully.")
    except Exception as e:
        print(f"Error while disabling recent files feature: {e}")

def disable_task_view_timeline():
    try:
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Privacy"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "TailoredExperiencesWithDiagnosticDataEnabled", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print("Visualizzazione delle attività disabilitata con successo.")
    except Exception as e:
        print(f"Errore durante la disattivazione della Visualizzazione delle attività: {e}")

def disable_search_history():
    try:
        key_path = r"Software\Policies\Microsoft\Windows\Explorer"
        # Apri o crea la chiave di registro
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        # Imposta il valore DWORD
        winreg.SetValueEx(key, "DisableSearchBoxSuggestions", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
        print("Cronologia di ricerca in Esplora File disabilitata con successo.")
    except Exception as e:
        print(f"Errore durante la disattivazione della cronologia di ricerca: {e}")


# Example usage:
device_input_dalay()
improve_screencapture()
improve_ping()
optimize_disk()
disable_uac()
disable_windows_defender()
disable_firewall()
disable_notifications()
disable_onedrive()
enable_show_hidden_files()
enable_auto_date_time()
disable_recent_files()
disable_task_view_timeline()
disable_search_history()

