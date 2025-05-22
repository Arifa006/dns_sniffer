from scapy.all import sniff, DNS, DNSQR, DNSRR
from colorama import init, Fore
from collections import defaultdict

# Initialize color output for Windows
init()

# Dictionary to store domain → IP mappings
domain_ip_map = defaultdict(set)

def process_packet(packet):
    if packet.haslayer(DNS):
        dns_layer = packet[DNS]
        domain = packet[DNSQR].qname.decode("utf-8")

        # Handle DNS Query
        if dns_layer.qr == 0:
            print(Fore.CYAN + f"[DNS Query] Requested domain: {domain}" + Fore.RESET)

        # Handle DNS Response
        elif dns_layer.qr == 1:
            new_ips = []
            for i in range(dns_layer.ancount):
                rr = dns_layer.an[i]
                if rr.type == 1:  # A record (IPv4)
                    ip = rr.rdata
                    new_ips.append(ip)

                    # Check for spoofed response
                    if ip not in domain_ip_map[domain]:
                        if domain_ip_map[domain]:  # domain already seen
                            print(Fore.RED + f"[!] ALERT: {domain} returned a new IP → {ip} (Possible Spoofing!)" + Fore.RESET)
                            # Log the alert to a file (UTF-8)
                            with open("dns_alerts.log", "a", encoding="utf-8") as log_file:
                                log_file.write(f"[{domain}] → {ip} (Possible Spoofing)\n")
                        domain_ip_map[domain].add(ip)

            if new_ips:
                print(Fore.GREEN + f"[DNS Response] {domain} → {', '.join(map(str, new_ips))}" + Fore.RESET)

# Start sniffing
print(Fore.YELLOW + "[*] DNS Spoof Detector Running..." + Fore.RESET)
sniff(filter="udp port 53", prn=process_packet, store=0)
