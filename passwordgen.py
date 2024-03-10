import random
import string

def generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        pwdlength = int(input("Enter the desired length of the password: "))
        if pwdlength > 0:
            generated_password = generate(pwdlength)
            print("Generated Password:", generated_password)
        else:
            print("Please enter a valid positive length for the password.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()