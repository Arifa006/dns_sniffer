A DNS Spoof Detection tool built using Python and Scapy


# 🛡️ DNS Spoof Detector

Hi! I built this **DNS Spoof Detection** tool as part of my learning journey in cybersecurity and networking. It’s a lightweight Python-based tool that listens to DNS traffic on the network and detects signs of **DNS spoofing** in real-time using the `Scapy` library.

This project helped me apply core concepts from network security, packet sniffing, and protocol analysis in a practical and hands-on way.

---

## 📌 What it Does

- 🧠 Listens to DNS responses using a packet sniffer
- 🔎 Checks for inconsistent IPs returned for the same domain
- 🚨 Displays terminal alerts for possible spoofed responses
- 📝 Logs suspicious activity to `dns_alerts.log` for further analysis

---

## 🗂️ Files Included

| File              | Description                                  |
|-------------------|----------------------------------------------|
| `dns_sniffer.py`  | Main Python script that runs the detector    |
| `dns_alerts.log`  | Log file that stores alerts on suspicious DNS activity |
| `README.md`       | Project overview and usage guide             |

---

## ▶️ How to Run

### 1. Install Requirements
Make sure Python 3 is installed on your machine, then install `Scapy`:

```bash
pip install scapy

### 2. Run the Detector
bash
python dns_sniffer.py

You’ll see:
css
[*] DNS Spoof Detector Running...
And if spoofing is detected:

[!] ALERT: www.example.com returned a new IP → 123.45.67.89 (Possible Spoofing!)


🧪 Sample Outputs

✅ Normal DNS Responses
[DNS Response] www.google.com → 142.251.41.36
[DNS Response] cdn.cloudflare.com → 104.17.210.9

⚠️ Spoofing Alerts
[!] ALERT: www.google.com returned a new IP → 23.45.67.89 (Possible Spoofing!)
[!] ALERT: www.yahoo.com returned a new IP → 54.23.111.5 (Possible Spoofing!)
