#Day 12: Working with JSON
#Project: A script that reads a JSON file or string and prints out specific values based on user input.
#A project to demonstrate how to parse and create JSON data using Python’s json library.

#Step 1: Import the JSON library 
import json

#Step 2: Create a JSON string (simulating reading from a file)
json_data = '''
{
    "users": [
        {"name": "Moyaq", "age": 20, "email": "moyaq20@gmail.com"},
        {"name": "Jay", "age": 22, "email": "jay22@yahoo.com"},
        {"name": "Irving", "age": 28, "email": "irving28@outlook.com"}
    ]
}
'''

#Step 3: Parse (convert) the JSON string into a Python dictionary
data = json.loads(json_data)

#Step 4: Function to search for a user and display their details
def search_user():
    while True:
        user_name = input("\nEnter a name to get details (or type 'exit' to quit): ").strip()

        if user_name.lower() == 'exit':
            print("Exiting the program. Cheerio!")
            break

#Search for the user in the list
        found = False
        for user in data["users"]:
            if user["name"].lower() == user_name.lower():
                print(f"\nName: {user['name']}")
                print(f"Age: {user['age']}")
                print(f"Email: {user['email']}")
                found = True
                break
        
        if not found:
            print(f"\nUser '{user_name}' not found. Please try again.")

#Main Program
if __name__ == "__main__":
    print("Welcome to the JSON User Lookup Program!")
    print("This program reads JSON data and allows you to retrieve user details.")

    search_user()
