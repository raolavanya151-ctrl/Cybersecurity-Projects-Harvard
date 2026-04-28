"""
Advanced Multithreaded Network Scanner
Scans ports 1–1024 on a target IP or domain using threading
"""

import socket
import threading
from queue import Queue

# Ask user for target
target = input("Enter target IP or domain: ")

# Convert domain to IP
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("❌ Invalid target. Please enter a valid IP or domain.")
    exit()

print(f"\n🔍 Scanning target: {target_ip}")
print("🚀 Scanning ports 1–1024...\n")

# Queue for ports
queue = Queue()
open_ports = []

# Lock for thread-safe printing
lock = threading.Lock()

def scan_port():
    while not queue.empty():
        port = queue.get()

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            result = sock.connect_ex((target_ip, port))

            if result == 0:
                with lock:
                    print(f"✅ Port {port}: OPEN")
                    open_ports.append(port)

            sock.close()

        except:
            pass

        finally:
            queue.task_done()

# Fill queue with ports
for port in range(1, 1025):
    queue.put(port)

# Create threads
thread_count = 50

for _ in range(thread_count):
    thread = threading.Thread(target=scan_port)
    thread.daemon = True
    thread.start()

# Wait for all threads to finish
queue.join()

# Final result
print("\n🎯 Scanning complete.")
print(f"🔓 Open ports: {open_ports if open_ports else 'None found'}")
