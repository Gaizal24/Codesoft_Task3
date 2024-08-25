#<------------------------------------Password Generator ---------------------------------->

import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if length < 1:
        print("Password length must be at least 1.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")

    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_numbers, use_special)
    
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    password_generator()
