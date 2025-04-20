import random
import string

def generate_password(length=12):
    if length < 6:
        print("⚠️ Password should be at least 6 characters long.")
        return ""

    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    
    all_characters = lowercase + uppercase + digits + symbols

    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]


    password += random.choices(all_characters, k=length - 4)


    random.shuffle(password)

    return ''.join(password)

def main():
    print("🔐 Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print("✅ Your secure password is:", password)
    except ValueError:
        print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    main()
