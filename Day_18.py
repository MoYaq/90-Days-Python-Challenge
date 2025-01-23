#Day 18: Introduction to Cryptography
#Project: Password Hashing and Verification
#A project to demonstrate how to hash and compare passwords using Python's hashlib library.

#Step 1: Import the hashlib library
import hashlib

#Step 2: Define a function to hash a password using SHA-256
def hash_password(password):
#Encode the password and hash it using SHA-256
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

#Step 3: Define a function to verify a password against a stored hash
def verify_password(stored_hash, user_password):
#Hash the user-entered password
    user_hash = hash_password(user_password)

#Compare it to the stored hash
    return user_hash == stored_hash

#Step 4: Define the main function
if __name__ == "__main__":
    print("Welcome to the Password Hasher and Verifier!\n")

#Step 5: Prompt the user to enter a password
    user_password = input("Enter a password to hash: ").strip()

#Step 6: Hash the password and display the hash
    hashed_password = hash_password(user_password)
    print(f"\nYour hashed password (SHA-256): {hashed_password}")

#Step 7: Ask for verification
    check_password = input("\nRe-enter your password to verify: ").strip()

#Step 8: Verify the password
    if verify_password(hashed_password, check_password):
        print("\nPassword verification successful! The passwords match.")
    else:
        print("\nPassword verification failed! The passwords do not match.")