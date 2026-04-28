import socket

target = input("Enter target IP or domain: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid target")
    exit()

print(f"\nScanning target: {target_ip}")
print("Scanning ports 1–1024...\n")

for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = sock.connect_ex((target_ip, port))

    if result == 0:
        print(f"Port {port}: OPEN")

    sock.close()

print("\nScanning complete.")
