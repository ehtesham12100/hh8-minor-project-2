import base64
from cryptography.fernet import Fernet
from hashlib import sha256

def generate_key(master_password):
    key = sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_data(data, master_password):
    key = generate_key(master_password)
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(encrypted_data, master_password):
    key = generate_key(master_password)
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()
