#Day 8: File I/O
#Project: Read a text file, create or modify it if necessary, and count the number of lines and words.
#A program to demonstrate how to read and write files in Python using open(), read(), write(). As well as well as how to work with text and CSV files. 
# Step 1: Function to write or append content to a fil
def write_to_file(file_name, mode="w"):
    try:
        # Open the file in the specified mode ("w" for overwrite, "a" for append)
        with open(file_name, mode) as file:
            print(f"\nEnter content for the file '{file_name}' (type 'STOP' on a new line to finish):")
            while True:
                line = input()
                if line.strip().upper() == "STOP":
                    break
                file.write(line + "\n")
        print(f"\nContent has been written to '{file_name}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Step 2: Function to count lines and words
def count_lines_and_words(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.readlines()

        line_count = len(content)
        word_count = sum(len(line.split()) for line in content)

        return line_count, word_count

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

# Step 3: Main program
if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Create a new file or overwrite an existing file")
        print("2. Append content to an existing file")
        print("3. Analyze a file (count lines and words)")
        print("4. Exit")
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            file_name = input("\nEnter the name of the file to create or overwrite: ").strip()
            write_to_file(file_name, mode="w")

        elif choice == "2":
            file_name = input("\nEnter the name of the file to append content: ").strip()
            write_to_file(file_name, mode="a")

        elif choice == "3":
            file_name = input("\nEnter the name of the file to analyze: ").strip()
            lines, words = count_lines_and_words(file_name)
            if lines is not None and words is not None:
                print(f"\nFile Analysis of '{file_name}':")
                print(f"Total Lines: {lines}")
                print(f"Total Words: {words}")

        elif choice == "4":
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")