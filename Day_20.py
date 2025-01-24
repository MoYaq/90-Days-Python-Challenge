#Day 20: Introduction to Encryption
#Project: Create A Simple Decryption Tool
#A Program to Demonstrate AES Decryption

#Step 1: Import the cryptography library
from cryptography.fernet import Fernet

#Step 2: Load the secret key
def load_key():
    return open("secret.key", "rb").read()

#Step 3: Decrypt an encrypted message
def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message.encode())
    return decrypted_message.decode()

#Main program
if __name__ == "__main__":
    print("AES Decryption Program")

#Load the existing key
    key = load_key()

#Get user input and decrypt
    encrypted_text = input("\nEnter the encrypted message: ")

    try:
        decrypted = decrypt_message(encrypted_text, key)
        print(f"\nDecrypted Message: {decrypted}")
    except Exception as e:
        print("\nInvalid key or encrypted text! Decryption failed.")