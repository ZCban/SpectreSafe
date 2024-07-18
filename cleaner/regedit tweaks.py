import winreg

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


device_input_dalay()
improve_screencapture()
improve_ping()
optimize_disk()
