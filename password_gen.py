
# Password Generator
import string
import random

def passwd_gen(length):
    if length < 4:
        raise ValueError("Password length must be atleast 4 characters.")

    # Passwords characters Set
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_char = string.punctuation
    
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_char)
    ]
    
    allChars = uppercase + lowercase + digits + special_char
    password += random.choices(allChars, k=length-4)
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome, this is the random password generator")
    try:
        length = int(input("Enter the desired length of the password. Must be above 4 characters."))
        password = passwd_gen(length)
        print(f"Your generated is: \n{password}")
    except ValueError as e:
        print(f"Error {e}")

if __name__ == "__main__":
    main()