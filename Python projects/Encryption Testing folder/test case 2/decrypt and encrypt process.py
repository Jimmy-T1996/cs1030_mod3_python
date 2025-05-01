from cryptography.fernet import Fernet

def key_loader():
    with open('mykey.key', 'rb') as key_file:
        return key_file.read()

def decrypt_file():
    key = key_loader()
    f = Fernet(key)

    with open('Password.csv', 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open('Password.csv', 'wb') as file:
        file.write(decrypted_data)

def encrypt_file():
    key = key_loader()
    f = Fernet(key)

    with open('Password.csv', 'rb') as file:
        decrypted_data = file.read()

    encrypted_data = f.encrypt(decrypted_data)

    with open('Password.csv', 'wb') as file:
        file.write(encrypted_data)

# Main program flow
decrypt_file()

# Now secrets.txt is decrypted. You can work with it!
with open('Password.csv', 'r') as file:
    secrets = file.read()

print(secrets)

input("\n🔒 Press Enter to encrypt and close...")

encrypt_file()

print("✅ File encrypted again. Bye!")
