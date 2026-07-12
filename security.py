from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

# Generate key (only once)
def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)

# Load key
def load_key():
    with open(KEY_FILE, "rb") as file:
        return file.read()

# Encrypt model
def encrypt_model():
    generate_key()
    key = load_key()
    f = Fernet(key)

    with open("model.pkl", "rb") as file:
        model = file.read()

    encrypted = f.encrypt(model)

    with open("model.encrypted", "wb") as file:
        file.write(encrypted)

    print("Model Encrypted Successfully!")

# Decrypt model
def decrypt_model():
    key = load_key()
    f = Fernet(key)

    with open("model.encrypted", "rb") as file:
        encrypted = file.read()

    decrypted = f.decrypt(encrypted)

    with open("model.pkl", "wb") as file:
        file.write(decrypted)

    print("Model Decrypted Successfully!")

if __name__ == "__main__":
    encrypt_model()