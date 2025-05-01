from cryptography.fernet import Fernet

#info pulled from Misha SV https://www.youtube.com/watch?v=zWNA2ThkVT4

#This generates a key and saves the file.
def key_gen():
    key = Fernet.generate_key()

    with open('mykey.key', 'wb') as mykey:
        mykey.write(key)

def key_loader():
    with open('mykey.key', 'rb') as mykey:
        return mykey.read()

#This pulls existing key from file in same directory.
def show_key():
    key= key_loader()
    print(key) 

#This encrypts a file.
def encrypt_funct():
    key = key_loader()
    f = Fernet(key)

    with open('secrets.txt', 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open("enc_secrets.txt", 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
 
def decrypt_funct():
    key = key_loader()
    f = Fernet(key)

    with open('enc_secrets.txt', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open('dec_secrets.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted) 

encrypt_funct()
decrypt_funct()