#Day 12: Working with JSON
#Project: Create a script that reads a JSON file and prints out specific values based on user input.
#A project to demonstrate how to parse and create JSON data using Python’s json library.

#Step 1: Import the json module
import json

#Step 2: Function to load JSON data from a file
def load_json_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)  # Convert JSON file content to a dictionary
        return data
    except FileNotFoundError:
        print("\nError: The file was not found.")
        return None
    except json.JSONDecodeError:
        print("\nError: The file does not contain valid JSON.")
        return None

#Step 3: Function to retrieve and display a value based on user input
def get_value_from_json(data):
    while True:
        key = input("\nEnter a key to retrieve its value (or type 'exit' to quit): ").strip()

        if key.lower() == "exit":
            print("\nExiting program. Goodbye!")
            break

        if key in data:
            print(f"{key}: {data[key]}")
        else:
            print("\nInvalid key! Please enter a valid key from the JSON file.")

#Main Program
if __name__ == "__main__":
    print("Welcome to the JSON Reader!")
    print("This program reads a JSON file and retrieves values based on user input.")

#Load the JSON file
    json_data = load_json_file("data.json")

    if json_data:
        get_value_from_json(json_data)