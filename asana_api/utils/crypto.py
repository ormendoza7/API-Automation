from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_token(token: str, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(token.encode())

def decrypt_token(encrypted_token: bytes, key: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(encrypted_token).decode()
