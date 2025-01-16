#Day 11: Regular Expressions

#Project: Build a program that validates email addresses using regular expressions.

#A project to demonstrate how to use the re library in Python for pattern matching.

#Step 1: Import the regex library
import re  

#Step 2: Define the function to validate email addresses
def is_valid_email(email):

 #Regular expression pattern for a valid email
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

#Check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False

#Step 3: Prompt the user to enter an email
if __name__ == "__main__":
    print("Email Validator Program")
    while True:
        user_email = input("\nEnter an email address to validate (or type 'exit' to quit): ").strip()

        if user_email.lower() == 'exit':
            print("\nExiting the program. Goodbye!")
            break

#Step 4: Validate the email and display the result
        if is_valid_email(user_email):
            print("✅ Valid email address!")
        else:
            print("❌ Invalid email address! Please enter a correctly formatted email.")            