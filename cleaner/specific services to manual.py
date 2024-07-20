import subprocess

def set_service_manual(service_name):
    try:
        # Comando PowerShell per impostare il servizio in modalità manuale
        command = f'Set-Service -Name "{service_name}" -StartupType "Manual"'
        subprocess.run(['powershell', '-Command', command], check=True)
        print(f"Il servizio {service_name} è stato impostato su manuale.")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'impostazione del servizio {service_name}")

# Lista dei servizi da impostare su manuale
services_to_set_manual = [
    "vgc",                  # Valorant (Vanguard Anti-Cheat)
    "RiotClientServices",   # Riot Client Services
    "Riot Vanguard",        # Riot Vanguard (anti-cheat for Valorant)
    "EpicGamesLauncher",    # Epic Games Launcher
    "Steam Client Service", # Steam Client Service
    "Origin Client Service",# Origin Client Service
    "UplaySvc",             # Ubisoft Uplay Service
    "Rockstar Service",     # Rockstar Games Launcher Service
    "EasyAntiCheat",        # EasyAntiCheat Service
    "BattlEye",             # BattlEye Service
    "EAAntiCheatService",   # Battlefield Anti-Cheat Service
    "BFService",            # Battlefield Service
    "MinecraftLauncher",    # Minecraft Launcher
    "XblAuthManager",       # Xbox Live Authentication Manager
    "XblGameSave",          # Xbox Live Game Save
    "XboxNetApiSvc",        # Xbox Live Networking Service
    "XboxGipSvc",           # Xbox Accessory Management Service
    "GamingServices",       # Gaming Services
    "DeviceAssociationService", # Device Association Service
    "DeviceInstall",        # Device Install Service
    "PhoneSvc",             # Phone Service
    "SmsRouter",            # Routing di SMS
    "RadioMgr",             # Radio Management Service
    "RmSvc",                # Radio Management
    "BlizzardUpdateAgent",  # Blizzard Update Agent
    "Battle.net",           # Battle.net Desktop Application
    "TwitchService",        # Twitch Service
    "DiscordUpdate",        # Discord Updater
    "SpotifyWebHelper",     # Spotify Web Helper
    "AdobeUpdateService",   # Adobe Update Service
    "AdobeGCClient",        # Adobe Genuine Monitor Service
    "GoogleDrive",          # Google Drive File Stream
    "DropboxUpdate",        # Dropbox Updater
    "OneSyncSvc",           # OneDrive Sync Service
    "SlackUpdate",          # Slack Updater
    "gupdate",              # Google Update Service
    "gupdatem",             # Google Update Service (Machine-Wide)
    "MozillaMaintenance",   # Mozilla Maintenance Service
    "edgeupdate",           # Microsoft Edge Update Service
    "edgeupdatem",          # Microsoft Edge Update Service (Machine-Wide)
    "Opera Browser Assistant", # Opera Browser Assistant
    "BraveUpdate",          # Brave Update Service
    "ClickToRunSvc",        # Microsoft Office Click-to-Run Service
    "OfficeSvc",            # Microsoft Office Service
    "Fax",                  # Fax
    "seclogon",             # Secondary Logon
    "wisvc",                # Windows Insider Service
    "SCardSvr",             # Smart Card
    "WbioSrvc",             # Windows Biometric Service
    "RetailDemo",           # Retail Demo Service
]

# Imposta ciascun servizio in modalità manuale
for service in services_to_set_manual:
    set_service_manual(service)


