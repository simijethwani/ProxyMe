from cryptography.fernet import Fernet

def encrypt_audio(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        encrypted = fernet.encrypt(f.read())
    with open(file_path + ".enc", 'wb') as f:
        f.write(encrypted)
