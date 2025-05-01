from cryptography.fernet import Fernet

# Generate a key and save it
key = Fernet.generate_key()
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# Load the key
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

# Create Fernet object
fernet = Fernet(key)

# Read the original file
with open('secrets.txt', 'rb') as file:
    original_data = file.read()

# Encrypt the data
encrypted_data = fernet.encrypt(original_data)

# Write the encrypted data back
with open('secrets.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

print("✅ File encrypted successfully.")


