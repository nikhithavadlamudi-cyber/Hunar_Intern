import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]

    if all(not e for e in errors):
        return "Strong"
    elif sum(errors) <= 2:
        return "Okay"
    else:
        return "Weak"

while True:
    pwd = input("Enter a password to check (or type 'exit' to stop): ")
    if pwd.lower() == 'exit':
        break
    strength = check_password_strength(pwd)
    print(f"Password Strength: {strength}\n")