#Day 7: Dictionaries and Sets

#Project: Create a program that stores user information (name, age) in a dictionary and allows the user to retrieve it by providing the name.

#A program to demonstrate how to use dictionary methods like get(), keys(), values(), items(), pop(), and clear().

#Step 1: Initialize the dictionary to store user information
user_info = {}

#Step 2: Create a menu-driven program to perform the various operations
while True:
    print("\nPlease choose an option to:")
    print("1. Add a user")
    print("2. Retrieve user info")
    print("3. View all users")
    print("4. Remove a user")
    print("5. Clear all user info")
    print("6. Exit")

#Take the user's choice
    choice = input("\nPlease enter your choice (1-6): \n")
    
#Option 1: Add a new user
    if choice == "1":
        name = input("\nPlease enter your name: \n").strip()
        if name in user_info:
            print(f"\n{name} already exists in the database.")
        else:
            age = input("Please enter your age: \n").strip()
            user_info[name] = age
            print(f"\n{name} has been added to the database.")

#Option 2: Retrieve user information
    elif choice == "2":
        name = input("\nEnter the name of the user to retrieve: ").strip()
        age = user_info.get(name)  # Use get() to safely retrieve the value
        if age:
            print(f"\n{name}'s age is {age}.")
        else:
            print(f"\n{name} does not exist in the database.")

#Option 3: View all users
    elif choice == "3":
        if user_info:
            print("\nCurrent Users in the Database:")
            for name, age in user_info.items():  # Use items() to iterate through key-value pairs
                print(f"Name: {name}, Age: {age}")
        else:
            print("\nNo users in the database.")
            
#Option 4: Remove a user
    elif choice == "4":
        name = input("\nEnter the name of the user to remove: ").strip()
        if name in user_info:
            user_info.pop(name) #Use pop() to remove a specific key-value pair
            print(f"\n{name} has been removed from the database.")
        else:
            print(f"\n{name} does not exist in the database.")
            
#Option 5: Clear all user information
    elif choice == "5":
        confirmation = input("\nAre you sure you want to clear all user information? (yes/no): ").strip().lower()
        if confirmation == "yes":
            user_info.clear()  #Use clear() to remove all items from the dictionary
            print("\nAll user information has been cleared.")
        else:
            print("\nOperation canceled.")
            
#Option 6: Exit the program
    elif choice == "6":
        print("\nExiting the program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.")

#Addendum:
