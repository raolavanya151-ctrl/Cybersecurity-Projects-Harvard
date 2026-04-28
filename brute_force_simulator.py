import time

correct_password = "admin123"

password_list = ["123456", "password", "admin", "admin123", "letmein"]

def brute_force():
    for attempt in password_list:
        print(f"Trying password: {attempt}")
        time.sleep(1)

        if attempt == correct_password:
            print("Access Granted!")
            break
        else:
            print("Access Denied")

brute_force()
