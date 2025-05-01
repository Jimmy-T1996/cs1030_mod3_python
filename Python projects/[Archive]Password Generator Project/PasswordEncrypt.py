from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import base64

use_password = input("Please enter a password: ")
password = use_password.encode()

salt =b'J\x04~r\xf5\x8e\xc7-\xa2y\x00\x8d\xc6\xa1Y~'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password))
print(key.decode())
