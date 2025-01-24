#Day 19: Introduction to Encryption
#Project: Create A Simple Encryption Tool Using The Cryptography Library (eg. AES)
#A Program to Demonstrate AES Encryption

#Step 1: Import the cryptography library
from cryptography.fernet import Fernet

#Step 2: Generate and save a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

#Step 3: Load an existing key from the file
def load_key():
    return open("secret.key", "rb").read()

#Step 4: Encrypt a message using the key
def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

#Main program
if __name__ == "__main__":
    print("AES Encryption Program")

#Generate a new key (only run this once)
    key = generate_key()
    print("Encryption Key has been generated.")

#Get user input and encrypt
    message = input("\nEnter a message to encrypt: ")
    encrypted = encrypt_message(message, key)
    print(f"\nEncrypted Message: {encrypted.decode()}")