#Day 19: AES Encryption and Decryption
#Project: A Simple Encryption and Decryption Tool Using the Cryptography Library
#A program to demonstrate 

#Step 1: Import the cryptography library
from cryptography.fernet import Fernet

#Step 2: Generate and save a key (Only needs to be run once)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

#Step 3: Load an existing key from the file
def load_key():
    return open("secret.key", "rb").read()

#Step 4: Encrypt a message using AES
def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message.decode()  # Convert bytes to string for readability

#Step 5: Decrypt an encrypted message
def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message.encode())
    return decrypted_message.decode()

#Main program
if __name__ == "__main__":
    print("AES Encryption & Decryption Program")

#Check if the key file exists, if not, generate one
    try:
        key = load_key()
    except FileNotFoundError:
        print("\nKey not found! Generating a new encryption key...")
        generate_key()
        key = load_key()
        print("Encryption key has been generated and saved.")

#User chooses to encrypt or decrypt
    action = input("\nDo you want to (E)ncrypt or (D)ecrypt a message? ").strip().lower()

    if action == "e":
#Encrypt a message
        message = input("\nEnter a message to encrypt: ")
        encrypted = encrypt_message(message, key)
        print(f"\nEncrypted Message: {encrypted}")

    elif action == "d":
#Decrypt a message
        encrypted_text = input("\nEnter the encrypted message: ")

        try:
            decrypted = decrypt_message(encrypted_text, key)
            print(f"\nDecrypted Message: {decrypted}")
        except Exception as e:
            print("\nInvalid key or encrypted text! Decryption failed.")

    else:
        print("\nInvalid option! Please choose 'E' to encrypt or 'D' to decrypt.")