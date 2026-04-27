import re

def check_password(password):
    if len(password) < 8:
        return "Weak: Too short"
    if not re.search("[A-Z]", password):
        return "Weak: Add uppercase letter"
    if not re.search("[a-z]", password):
        return "Weak: Add lowercase letter"
    if not re.search("[0-9]", password):
        return "Weak: Add a number"
    if not re.search("[!@#$%^&*]", password):
        return "Weak: Add special character"
    return "Strong password"

pwd = input("Enter password: ")
print(check_password(pwd))
