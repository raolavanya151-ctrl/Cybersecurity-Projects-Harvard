import random
import string

def generate_password(length=12):
    if length < 8:
        return "Password length should be at least 8"

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
