# **Packet Sniffer**

### **Description:**

Welcome to the Python Packet Sniffer repository, a simple yet powerful network analysis tool built on the Scapy library. This tool captures, decodes, and presents real-time data packets, providing insights into network communication. Its user-friendly interface and filtering options make it ideal for efficient monitoring and analysis of network traffic.

### **Usage:**

1. Clone the repository.
2. Install dependencies: `pip install scapy`.
3. Run the script: `python packet_sniffer.py`.

### **Output Format:**

For each captured packet, the sniffer presents the following details:

- **Source IP:** The IP address of the packet's source.
- **Destination IP:** The IP address of the packet's destination.
- **Source Port:** The port from which the packet originates.
- **Destination Port:** The port to which the packet is directed.
- **Packet Contents:** A summary of the packet contents.

### **Example Output:**

```
Source IP: 192.***.*.2
Destination IP: 8.8.8.8
Source Port: 3****
Destination Port: 8****
Packet Contents: Ether / IP / TCP 192.***.*.2:3**** > 8.8.8.8:8****
```

## Contributing

Contributions are welcome! If you have suggestions for improvements, feature requests, or would like to report issues, feel free to [create an issue](https://github.com/Pranav-Amin-10/PacketSniffer/issues) or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
