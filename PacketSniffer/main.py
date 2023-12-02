import scapy.all as scapy


def sniff_and_save_packets(interface, output_file):
    try:
        while True:
            packet = scapy.sniff(iface=interface, count=1)[0]
            if scapy.IP in packet:
                save_packet_to_file(packet, output_file)
    except Exception as e:
        print(f"An error occurred: {e}")


def save_packet_to_file(packet, filename):
    with open(filename, "a") as file:
        file.write("Packet Details:\n")
        file.write(f"Source IP: {packet[scapy.IP].src}\n")
        file.write(f"Destination IP: {packet[scapy.IP].dst}\n")
        if scapy.TCP in packet:
            file.write(f"Source Port: {packet[scapy.TCP].sport}\n")
            file.write(f"Destination Port: {packet[scapy.TCP].dport}\n")
        elif scapy.UDP in packet:
            file.write(f"Source Port: {packet[scapy.UDP].sport}\n")
            file.write(f"Destination Port: {packet[scapy.UDP].dport}\n")
        file.write("Packet Contents:\n")
        file.write(str(packet) + "\n\n")


def main():
    interface = "Wi-Fi"  # Replace with your network interface name
    output_file = "D:\\Practicals\\Python\\PacketSniffer\\captured_packets.txt"

    print(f"Sniffing packets on interface {interface}... (Press Ctrl+C to stop)")
    sniff_and_save_packets(interface, output_file)


if __name__ == "__main__":
    main()
