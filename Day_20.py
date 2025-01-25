#Day 19-20: AES Encryption & Decryption using PyCryptodome
#Project: Create a simple encryption and decryption tool
#A program to demonstrate AES encryption and decryption

# Step 1: Import the necessary modules
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

# Step 2: Generate a random 16-byte key for encryption
def generate_key():
    key = os.urandom(16)  # AES requires a key size of 16, 24, or 32 bytes
    with open("aes_key.key", "wb") as key_file:
        key_file.write(key)
    return key

# Step 3: Load an existing AES key from the file
def load_key():
    return open("aes_key.key", "rb").read()

# Step 4: Encrypt a message using AES
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)  # Using CBC mode
    iv = cipher.iv  # Initialization vector
    encrypted_message = cipher.encrypt(pad(message.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_message).decode()

# Step 5: Decrypt an AES-encrypted message
def decrypt_message(encrypted_message, key):
    try:
        raw_data = base64.b64decode(encrypted_message)
        iv = raw_data[:16]  # Extract IV from the data
        encrypted_message = raw_data[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(encrypted_message), AES.block_size)
        return decrypted_message.decode()
    except Exception as e:
        return "Decryption failed! Invalid key or corrupted data."

# Main Program
if __name__ == "__main__":
    print("AES Encryption & Decryption Program")

    # Generate a key if it does not exist
    if not os.path.exists("aes_key.key"):
        key = generate_key()
        print("A new AES key has been generated.")
    else:
        key = load_key()

    # Encrypt a message
    message = input("\nEnter a message to encrypt: ")
    encrypted_text = encrypt_message(message, key)
    print(f"\nEncrypted Message: {encrypted_text}")

    # Decrypt the message
    decrypted_text = decrypt_message(encrypted_text, key)
    print(f"\nDecrypted Message: {decrypted_text}")