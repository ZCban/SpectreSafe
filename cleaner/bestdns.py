import dns.resolver
import time
import subprocess
import os

# Dizionario con i nomi dei provider DNS e i relativi indirizzi IP primari e secondari
dns_providers = {
    #'Fastweb': {'primary': '192.168.1.254', 'secondary': '192.168.1.254'},
    'Google': {'primary': '8.8.8.8', 'secondary': '8.8.4.4'},
    'Control D': {'primary': '76.76.2.0', 'secondary': '76.76.10.0'},
    'Quad9': {'primary': '9.9.9.9', 'secondary': '149.112.112.112'},
    'OpenDNS Home': {'primary': '208.67.222.222', 'secondary': '208.67.220.220'},
    'Cloudflare': {'primary': '1.1.1.1', 'secondary': '1.0.0.1'},
    'CleanBrowsing': {'primary': '185.228.168.9', 'secondary': '185.228.169.9'},
    #'Alternate DNS': {'primary': '76.76.19.19', 'secondary': '76.223.122.150'},
    'AdGuard DNS': {'primary': '94.140.14.14', 'secondary': '94.140.15.15'},
    'Norton DNS': {'primary': '199.85.126.20', 'secondary': '199.85.127.20'},
    #'FoxDNS Security': {'primary': '89.33.7.211', 'secondary': '185.53.128.131'},
}

# Dominio da risolvere per testare i DNS
domain_to_test = 'google.com'

def test_dns_speed(dns_server):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]
    
    start_time = time.time()
    try:
        resolver.resolve(domain_to_test)
        return time.time() - start_time
    except Exception as e:
        print(f"Errore nella risoluzione con {dns_server}: {e}")
        return float('inf')  # Ritorna un tempo molto alto in caso di errore

# Testa ciascun server DNS e raccogli i tempi di risposta
results = {}
for provider, addresses in dns_providers.items():
    primary_speed = test_dns_speed(addresses['primary'])
    secondary_speed = test_dns_speed(addresses['secondary'])
    
    results[provider] = {
        'primary': {'address': addresses['primary'], 'speed': primary_speed},
        'secondary': {'address': addresses['secondary'], 'speed': secondary_speed}
    }

    #print(f"{provider} - Primary DNS ({addresses['primary']}): {primary_speed:.4f} secondi")
    #print(f"{provider} - Secondary DNS ({addresses['secondary']}): {secondary_speed:.4f} secondi")
    #print()

# Stampa il provider DNS più veloce e il relativo indirizzo IP
fastest_provider = min(results, key=lambda x: min(results[x]['primary']['speed'], results[x]['secondary']['speed']))
fastest_primary_dns = results[fastest_provider]['primary']['address']
fastest_secondary_dns = results[fastest_provider]['secondary']['address']
print("==========================")
print(f"Il provider DNS più veloce è {fastest_provider} con il Primary DNS {fastest_primary_dns} ({results[fastest_provider]['primary']['speed']:.4f} secondi) e il Secondary DNS {fastest_secondary_dns} ({results[fastest_provider]['secondary']['speed']:.4f} secondi).")
print("=========================")
# Lista dei nomi dei processi dei browser
browser_processes = ["chrome.exe", "firefox.exe", "opera.exe", "brave.exe","msedge.exe","iexplore.exe"]

# Chiudi i processi dei browser
for browser_process in browser_processes:
    try:
        subprocess.run(["taskkill", "/F", "/IM", browser_process], check=True)
        #print(f"Chiuso il processo: {browser_process}")
    except subprocess.CalledProcessError as e:
        #print(f"probabile non installato o non in esecuzione {browser_process}: {e}")
        continue

# Imposta automaticamente i server DNS più veloci (esempio per Windows usando PowerShell)
try:
    subprocess.run(["powershell", "-Command", f"Set-DnsClientServerAddress -InterfaceIndex (Get-NetAdapter).InterfaceIndex -ServerAddresses @('{fastest_primary_dns}','{fastest_secondary_dns}')"])
    print("=====================================================")
    print("I server DNS sono stati impostati con successo.")
    print("=====================================================")
except Exception as e:
    print(f"Errore nell'impostazione dei server DNS: {e}")
