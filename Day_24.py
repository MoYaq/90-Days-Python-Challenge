#Day 24-25:Brute Force Password Cracking

#Project: Write a script that attempts to brute-force a password using a wordlist and hashes it with hashlib.

#A program to demonstrate how to use hashlib to hash a password and compare it to a hash stored in a file.

#Step 1:Import required libraries
import hashlib#imports hashlib for hashing passwords
import itertools#imports itertools for generating brute-force password combinations

#Step 2:Function to hash passwords using SHA256
def hash_password(password):
    """Returns the SHA256 hash of the given password."""
    return hashlib.sha256(password.encode()).hexdigest()

#Step 3:Function to check if a password exists in a wordlist
def check_wordlist(target_hash, wordlist_file):
    """Reads passwords from a wordlist and checks if any match the target hash.Returns the matching password if found, otherwise returns None."""
    try:
        with open(wordlist_file, 'r', encoding='utf-8') as file:
            for line in file:
                password=line.strip()#Removes whitespace/newlines
                if hash_password(password)==target_hash:
                    return password#Password found
    except FileNotFoundError:
        print("[-]Wordlist file not found.")
    return None#No match found

#Step 4:Function to brute-force passwords by generating combinations
def brute_force_attack(target_hash, charset, max_length):
    """Generates all possible password combinations using the given character set.Compares each generated password's hash with the target hash."""
    for length in range(1, max_length+1):#Start from length 1 up to max_length
        for attempt in itertools.product(charset, repeat=length):
            password=''.join(attempt)#Converts tuple to string
            if hash_password(password)==target_hash:
                return password#Password found
    return None#No match found

#Step 5:Main program execution
if __name__=="__main__":
    print("🔹Brute-Force Password Cracker🔹")

    #Step 6:Ask user for the target hashed password
    target_hash=input("\nEnter the target hash(SHA256): ")

    #Step 7:Ask if user wants to use a wordlist
    use_wordlist=input("Do you want to use a wordlist?(yes/no): ").lower()
    found_password=None#Initialize password variable

    #Step 8:If the user chooses to use a wordlist,check for matches
    if use_wordlist=="yes":
        wordlist_file=input("Enter the path to the wordlist file: ")
        found_password=check_wordlist(target_hash, wordlist_file)

    #Step 9:If wordlist fails,start brute-force attack
    if not found_password:
        print("\n[*]Wordlist failed.Starting brute-force attack...")
        charset="abcdefghijklmnopqrstuvwxyz0123456789"#Default character set
        max_length=int(input("Enter max password length for brute force: "))#Get max password length
        found_password=brute_force_attack(target_hash, charset, max_length)

    #Step 10:Display the results
    if found_password:
        print(f"\n[+]Password found: {found_password}")
    else:
        print("[-]Password not found.")