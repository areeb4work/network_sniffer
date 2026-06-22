# 🔍 Basic Network Sniffer

A Python-based network sniffer that captures and analyzes live network traffic in real time. Built to understand how data flows across a network and how packets are structured at the protocol level (TCP, UDP, ICMP). Useful for network monitoring, traffic analysis, and learning core cybersecurity concepts.

**Tools:** Python, Scapy, Npcap (Windows)

## Requirements

- Python 3.8+
- [Npcap](https://npcap.com/#download) (Windows only - install with WinPcap API-compatible mode checked)
- Scapy library

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/network-sniffer.git
cd network-sniffer

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install scapy
```

## Usage

Run with administrator/root privileges:

```bash
# Windows (run terminal as Administrator)
python sniffer.py

# Linux/Mac
sudo python3 sniffer.py
```

Press `Ctrl+C` to stop the sniffer.

## Example Output

```
Starting network sniffer... Press Ctrl+C to stop.

[12:30:15] 192.168.1.5 --> 142.250.183.78
Protocol: TCP | Src Port: 51234 | Dst Port: 443

[12:30:16] 192.168.1.5 --> 8.8.8.8
Protocol: UDP | Src Port: 54321 | Dst Port: 53

[12:30:17] 192.168.1.5 --> 192.168.1.1
Protocol: ICMP (ping)
```

## What I Learned

- How network packets are structured (IP, TCP, UDP, ICMP layers)
- Difference between TCP (reliable) vs UDP (fast) vs ICMP (diagnostics)
- How raw socket/packet capture works at a low level
- Port analysis and process identification on Windows
- Why HTTPS encryption protects against packet sniffing

## ⚠️ Legal Notice

This tool is intended for educational purposes only. Only use it on networks and systems you own or have explicit permission to monitor. Unauthorized packet sniffing is illegal.

## Author

**Areeb Ahsan**
Built as part of a Cybersecurity Internship at **Arch Technologies** — Month 1, Project 1
