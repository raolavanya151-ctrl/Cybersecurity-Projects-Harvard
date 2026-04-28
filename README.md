# Cybersecurity-Projects-Harvard
Cybersecurity projects and practical exercises demonstrating knowledge of networking, security concepts, and basic ethical hacking techniques.
## Certificate
![CS50 Certificate](IMG_2904.jpg)

## 🧠 Skills Demonstrated

- 🔐 Password Security & Validation  
- 🧠 Understanding of Brute Force Attacks  
- ⚙️ Python Scripting for Cybersecurity  
- 🛡️ Basic Ethical Hacking Concepts  

## Projects

### 🔐 Password Strength Checker (Python)

A simple cybersecurity tool that checks whether a password is strong or weak based on security rules.

**Features:**
- ✅ Minimum length check (8+ characters)
- ✅ Detects uppercase and lowercase letters
- ✅ Checks for numbers
- ✅ Checks for special characters
- ✅ Uses regex (pattern matching)

**Tech Used:**
- Python
- Regular Expressions (re module)

**Example Output:**
```text
Enter password: Hello123
Weak: add special character

Enter password: Hello@123
Strong password


---
## 🚀 How to Run

Follow these steps to run the cybersecurity tools locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/raolavanya151-ctrl/Cybersecurity-Projects-Harvard.git
cd Cybersecurity-Projects-Harvard
```

### 2️⃣ Run the projects

#### 🔐 Password Strength Checker
```bash
python password_checker.py
```

#### 🔐 Password Generator
```bash
python password_generator.py
```

#### 🧠 Login Brute Force Simulator
```bash
python brute_force_simulator.py
```

### 💡 Requirements
### 🌐 Network Scanner (Python)

A basic cybersecurity tool that scans a target system to identify open ports.

**Features:**
- 🔍 Scans ports 1–1024
- 🌐 Supports IP address and domain input
- ⚡ Detects open ports

**Tech Used:**
- Python
- Socket module

**Example Output:**
```text
Enter target IP or domain: google.com

Scanning target: 142.250.xxx.xxx
Scanning ports 1–1024...

Port 80: OPEN
Port 443: OPEN

Scanning complete.
- Python 3.x installed  
- Basic knowledge of running Python scripts (optional)
