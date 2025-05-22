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









SCREENSHOTS 

✅ 1. Running.png
What it shows:

The tool has been successfully launched and is actively monitoring DNS traffic.

Why it matters:
This proves your script is functional and correctly set up — important for beginners or recruiters who need to see that it runs without errors.

🌐 2. Dns query response Alert possible spoofing.png
What it shows:

Real-time DNS queries

Multiple IP responses

Alert flagging for possible spoofing

Why it matters:
This is the core demonstration of your project. It shows the detection logic working and alerting correctly — a big highlight.

🚨 3. Spoof Alert Detection.png
What it shows:

A close-up zoomed view of a spoof detection alert

A clear red [!] ALERT: line with a suspicious IP

Why it matters:
This reinforces your detection result, shows precision in matching IP inconsistencies, and highlights red-flagging for spoofing.



