def block_telemetry_domains():
    try:
        with open(r'C:\Windows\System32\drivers\etc\hosts', 'a') as hosts_file:
            domains = [
                # Windows
                "127.0.0.1 vortex.data.microsoft.com",
                "127.0.0.1 vortex-win.data.microsoft.com",
                "127.0.0.1 telecommand.telemetry.microsoft.com",
                "127.0.0.1 telecommand.telemetry.microsoft.com.nsatc.net",
                "127.0.0.1 oca.telemetry.microsoft.com",
                "127.0.0.1 oca.telemetry.microsoft.com.nsatc.net",
                "127.0.0.1 sqm.telemetry.microsoft.com",
                "127.0.0.1 sqm.telemetry.microsoft.com.nsatc.net",
                "127.0.0.1 a-0001.a-msedge.net",
                "127.0.0.1 a-0002.a-msedge.net",
                "127.0.0.1 a-0003.a-msedge.net",
                "127.0.0.1 a-0004.a-msedge.net",
                "127.0.0.1 a-0005.a-msedge.net",
                "127.0.0.1 a-0006.a-msedge.net",
                "127.0.0.1 a-0007.a-msedge.net",
                "127.0.0.1 a-0008.a-msedge.net",
                "127.0.0.1 a-0009.a-msedge.net",
                "127.0.0.1 a-msedge.net",
                "127.0.0.1 asimov-win.settings.data.microsoft.com",
                "127.0.0.1 content.windows.microsoft.com",
                "127.0.0.1 df.telemetry.microsoft.com",
                "127.0.0.1 diagnostic.data.microsoft.com",
                "127.0.0.1 dl.delivery.mp.microsoft.com",
                "127.0.0.1 geo.settings.data.microsoft.com",
                "127.0.0.1 i1.services.social.microsoft.com",
                "127.0.0.1 i1.services.social.microsoft.com.nsatc.net",
                "127.0.0.1 ipv6.msftconnecttest.com",
                "127.0.0.1 msedge.net",
                "127.0.0.1 msnbot-65-55-108-23.search.msn.com",
                "127.0.0.1 msntest.serving-sys.com",
                "127.0.0.1 oca.telemetry.microsoft.com",
                "127.0.0.1 oca.telemetry.microsoft.com.nsatc.net",
                "127.0.0.1 pre.footprintpredict.com",
                "127.0.0.1 redir.metaservices.microsoft.com",
                "127.0.0.1 reports.wes.df.telemetry.microsoft.com",
                "127.0.0.1 services.wes.df.telemetry.microsoft.com",
                "127.0.0.1 settings-sandbox.data.microsoft.com",
                "127.0.0.1 settings-win.data.microsoft.com",
                "127.0.0.1 sqm.df.telemetry.microsoft.com",
                "127.0.0.1 sqm.telemetry.microsoft.com",
                "127.0.0.1 ssw.live.com",
                "127.0.0.1 statsfe1.ws.microsoft.com",
                "127.0.0.1 survey.watson.microsoft.com",
                "127.0.0.1 telecommand.telemetry.microsoft.com",
                "127.0.0.1 telecommand.telemetry.microsoft.com.nsatc.net",
                "127.0.0.1 telemetry.appex.bing.net",
                "127.0.0.1 telemetry.microsoft.com",
                "127.0.0.1 telemetry.urs.microsoft.com",
                "127.0.0.1 vortex-sandbox.data.microsoft.com",
                "127.0.0.1 vortex-win.data.microsoft.com",
                "127.0.0.1 watson.live.com",
                "127.0.0.1 watson.microsoft.com",
                "127.0.0.1 watson.ppe.telemetry.microsoft.com",
                "127.0.0.1 wes.df.telemetry.microsoft.com",
                "127.0.0.1 willcroftg.services.ms",
                "127.0.0.1 www.msftncsi.com",
                
                # Discord
                "127.0.0.1 discordapp.com",
                "127.0.0.1 www.discordapp.com",
                "127.0.0.1 cdn.discordapp.com",
                "127.0.0.1 status.discordapp.com",
                "127.0.0.1 telemetry.discordapp.com",
                
                # Nvidia
                "127.0.0.1 telemetry.nvidia.com",
                "127.0.0.1 gfe.nvidia.com",
                "127.0.0.1 services.gfe.nvidia.com",
                "127.0.0.1 telemetry.gfe.nvidia.com",
                "127.0.0.1 events.gfe.nvidia.com",
                
                # Valorant
                "127.0.0.1 data.riotgames.com",
                "127.0.0.1 telemetry.riotgames.com",
                "127.0.0.1 log-ingestion.riotgames.com",
                "127.0.0.1 metrics.riotgames.com",
                "127.0.0.1 tracking.riotgames.com",
                "127.0.0.1 data.valorant.com",
                "127.0.0.1 telemetry.valorant.com",
                "127.0.0.1 log-ingestion.valorant.com",
                "127.0.0.1 metrics.valorant.com",
                "127.0.0.1 tracking.valorant.com",
                
                # Steam
                "127.0.0.1 telemetry.steampowered.com",
                "127.0.0.1 metrics.steampowered.com",
                "127.0.0.1 stats.steampowered.com",
                "127.0.0.1 data.steampowered.com",
                "127.0.0.1 beacon.steampowered.com",
                "127.0.0.1 steamtelemetry.com",
                "127.0.0.1 steamtelemetry.net",
                
                # Rust
                "127.0.0.1 telemetry.facepunch.com",
                "127.0.0.1 stats.facepunch.com",
                "127.0.0.1 analytics.facepunch.com",
                "127.0.0.1 data.facepunch.com",
                "127.0.0.1 events.facepunch.com",
                "127.0.0.1 beacon.facepunch.com",
                
                # Fortnite ed Epic Games
                "127.0.0.1 telemetry.epicgames.com",
                "127.0.0.1 telemetry.fortnite.com",
                "127.0.0.1 analytics.fortnite.com",
                "127.0.0.1 analytics.epicgames.com",
                "127.0.0.1 data.epicgames.com",
                "127.0.0.1 data.fortnite.com",
                "127.0.0.1 events.epicgames.com",
                "127.0.0.1 events.fortnite.com",
                "127.0.0.1 tracking.epicgames.com",
                "127.0.0.1 tracking.fortnite.com",
                
                # Apex Legends
                "127.0.0.1 telemetry.apexlegends.com",
                "127.0.0.1 metrics.apexlegends.com",
                "127.0.0.1 analytics.apexlegends.com",
                "127.0.0.1 data.apexlegends.com",
                "127.0.0.1 events.apexlegends.com",
                "127.0.0.1 tracking.apexlegends.com",
                "127.0.0.1 beacon.apexlegends.com",
                "127.0.0.1 telemetry.ea.com",
                "127.0.0.1 metrics.ea.com",
                "127.0.0.1 analytics.ea.com",
                "127.0.0.1 data.ea.com",
                "127.0.0.1 events.ea.com",
                "127.0.0.1 tracking.ea.com",
                "127.0.0.1 beacon.ea.com",
                
                # PUBG
                "127.0.0.1 telemetry.pubg.com",
                "127.0.0.1 metrics.pubg.com",
                "127.0.0.1 analytics.pubg.com",
                "127.0.0.1 data.pubg.com",
                "127.0.0.1 events.pubg.com",
                "127.0.0.1 tracking.pubg.com",
                "127.0.0.1 beacon.pubg.com",
                
                # Farlight 84
                "127.0.0.1 telemetry.farlight84.com",
                "127.0.0.1 metrics.farlight84.com",
                "127.0.0.1 analytics.farlight84.com",
                "127.0.0.1 data.farlight84.com",
                "127.0.0.1 events.farlight84.com",
                "127.0.0.1 tracking.farlight84.com",
                "127.0.0.1 beacon.farlight84.com",
                
                # Genshin Impact
                "127.0.0.1 log-upload-os.mihoyo.com",
                "127.0.0.1 overseauspider.yuanshen.com",
                "127.0.0.1 oslog-upload.mihoyo.com",
                "127.0.0.1 log-upload.mihoyo.com",
                "127.0.0.1 gitelemetry.gi.e.dhs.mihoyo.com",
                "127.0.0.1 log-upload-genshin.mihoyo.com",
                "127.0.0.1 os-genshin.mihoyo.com",
                
                # League of Legends
                "127.0.0.1 l3cdn.riotgames.com",
                "127.0.0.1 l3cdn.lol.riotgames.com",
                "127.0.0.1 l3cdn.na.lol.riotgames.com",
                "127.0.0.1 l3cdn.euw.lol.riotgames.com",
                "127.0.0.1 l3cdn.eune.lol.riotgames.com",
                
                # Call of Duty
                "127.0.0.1 telemetry.callofduty.com",
                "127.0.0.1 metrics.callofduty.com",
                "127.0.0.1 analytics.callofduty.com",
                "127.0.0.1 data.callofduty.com",
                "127.0.0.1 events.callofduty.com",
                "127.0.0.1 tracking.callofduty.com",
                "127.0.0.1 beacon.callofduty.com",
                
                # FIFA
                "127.0.0.1 telemetry.fifa.com",
                "127.0.0.1 metrics.fifa.com",
                "127.0.0.1 analytics.fifa.com",
                "127.0.0.1 data.fifa.com",
                "127.0.0.1 events.fifa.com",
                "127.0.0.1 tracking.fifa.com",
                "127.0.0.1 beacon.fifa.com"
            ]
            
            for domain in domains:
                hosts_file.write(f"{domain}\n")
            
            print("Domains successfully added to the hosts file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Esegui la funzione per bloccare i domini di telemetria
block_telemetry_domains()
