# Day 7: Dictionaries and Sets

#Project: Create a program that stores user information (name, age) in a dictionary and allows the user to retrieve it by providing the name.

#A program to demonstrate how to use dictionary methods like get(), keys(), values(), items(), pop(), and clear().

#Step 1: Initialize the dictionary to store user information
user_info = {}

#Step 2: Create a menu-driven program to perform the various operations
while True:
    print("\nSelect an option:")
    print("1. Add a new user")
    print("2. Retrieve user information")
    print("3. View all users")
    print("4. Remove a user")
    print("5. Clear all user information")
    print("6. Exit")

#Take the user's choice
    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
#Add a new user
        name = input("\nEnter the user's name: ").strip()
        if name in user_info:
            print(f"\n{name} already exists in the database.")
        else:
            age = input("Enter the user's age: ").strip()
            user_info[name] = age
            print(f"\n{name} has been added to the database.")

    elif choice == "2":
#Retrieve user information
        name = input("\nEnter the name of the user to retrieve: ").strip()
        age = user_info.get(name)  # Use get() to safely retrieve the value
        if age:
            print(f"\n{name}'s age is {age}.")
        else:
            print(f"\n{name} does not exist in the database.")

    elif choice == "3":
#View all users
        if user_info:
            print("\nCurrent Users in the Database:")
            for name, age in user_info.items():  # Use items() to iterate through key-value pairs
                print(f"Name: {name}, Age: {age}")
        else:
            print("\nNo users in the database.")

    elif choice == "4":
#Remove a user
        name = input("\nEnter the name of the user to remove: ").strip()
        if name in user_info:
            user_info.pop(name) #Use pop() to remove a specific key-value pair
            print(f"\n{name} has been removed from the database.")
        else:
            print(f"\n{name} does not exist in the database.")

    elif choice == "5":
#Clear all user information
        confirmation = input("\nAre you sure you want to clear all user information? (yes/no): ").strip().lower()
        if confirmation == "yes":
            user_info.clear()  #Use clear() to remove all items from the dictionary
            print("\nAll user information has been cleared.")
        else:
            print("\nOperation canceled.")

    elif choice == "6":
#Exit the program
        print("\nExiting the program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.")

#Addendum: