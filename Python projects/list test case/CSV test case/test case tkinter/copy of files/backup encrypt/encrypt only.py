from cryptography.fernet import Fernet

# Load or create key
def key_loader():
    with open('mykey.key', 'rb') as key_file:
        return key_file.read()

def key_gen():
    key = Fernet.generate_key()
    with open('mykey.key', 'wb') as key_file:
        key_file.write(key)
    return key

# Encrypt the file for the first time
def encrypt_file_first_time():
    try:
        key = key_loader()
    except FileNotFoundError:
        key = key_gen()

    f = Fernet(key)

    with open('Password.csv', 'rb') as file:
        data = file.read()

    encrypted_data = f.encrypt(data)

    with open('Password.csv', 'wb') as file:
        file.write(encrypted_data)

encrypt_file_first_time()

print("✅ secrets.txt encrypted for the first time.")


