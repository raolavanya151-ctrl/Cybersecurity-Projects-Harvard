---

### 🌐 Network Scanner (Python)

A multithreaded cybersecurity tool that scans a target system to identify open ports.

**Features:**
- Scans ports 1–1024
- Detects open ports
- Supports both IP address and domain input
- Fast scanning using multithreading

**Tech Used:**
- Python
- socket module
- threading module

**Example Output:**
```text
Enter target IP or domain: google.com

Scanning target: 142.250.xxx.xxx
Scanning ports 1–1024...

Port 80: OPEN
Port 443: OPEN

Scanning complete.
```
