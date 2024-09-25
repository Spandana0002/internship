import string
import random

def generate_password(length):
    """Generate a random password of the given length."""
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation 

    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    
    password = ''.join(random.choice(s) for _ in range(length))
    return password

def main():
    while True:
        password_length = input("Enter the length of the password (or break to stop):\n")
        if password_length.lower() == 'break':
            break
        try:
            password_length = int(password_length)
            password = generate_password(password_length)
            print("Your password is:")
            print(password)
        except ValueError:
            print("Invalid input. Please enter a number or 'break' to stop.")

if __name__ == "__main__":
    main()