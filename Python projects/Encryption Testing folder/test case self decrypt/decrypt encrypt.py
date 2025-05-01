from cryptography.fernet import Fernet

# Load the key
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

# Create Fernet object
fernet = Fernet(key)

# Read the encrypted file
with open('secrets.txt', 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()

# Decrypt the data
decrypted_data = fernet.decrypt(encrypted_data)

# Show the decrypted content
print("📄 Decrypted contents of secrets.txt:")
print(decrypted_data.decode())

input("\n🔒 Press Enter to re-encrypt the file...")

# Re-encrypt the data
reencrypted_data = fernet.encrypt(decrypted_data)

# Save the re-encrypted data
with open('secrets.txt', 'wb') as encrypted_file:
    encrypted_file.write(reencrypted_data)

print("✅ File re-encrypted successfully.")
