import socket

def scan_ports():
    host = input("Enter IP Address: ")

    ports = [21, 22, 23, 80, 443]

    print("\nScanning...\n")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is OPEN")

        sock.close()
        