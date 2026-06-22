from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

def analyze_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"\n[{timestamp}] {src_ip} --> {dst_ip}")

        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"Protocol: TCP | Src Port: {tcp_layer.sport} | Dst Port: {tcp_layer.dport}")
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"Protocol: UDP | Src Port: {udp_layer.sport} | Dst Port: {udp_layer.dport}")
        elif ICMP in packet:
            print("Protocol: ICMP (ping)")
        else:
            print(f"Protocol: Other (proto number {proto})")

        if packet.haslayer('Raw'):
            payload = packet['Raw'].load
            print(f"Payload size: {len(payload)} bytes")

def main():
    print("Starting network sniffer... Press Ctrl+C to stop.\n")
    try:
        sniff(prn=analyze_packet, store=False)
    except PermissionError:
        print("Error: Run this script with administrator/root privileges.")
    except KeyboardInterrupt:
        print("\nSniffer stopped.")

if __name__ == "__main__":
    main()