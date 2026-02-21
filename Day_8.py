#Day 8: File I/O
#Project: Write a script that reads a text file and counts how many lines and words are in the file.
#A program to demonstrate how to use open(), read(), write(), and Python's csv module.

import csv

#Function to write or append to a text file
def write_to_text_file(file_name, mode="w"):
    try:
        with open(file_name, mode) as file:
            print(f"\nEnter content for the text file '{file_name}' (type 'STOP' on a new line to finish):")
            while True:
                line = input()
                if line.strip().upper() == "STOP":
                    break
                file.write(line + "\n")
        print(f"\nContent has been written to the text file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred while writing to the text file: {e}")

#Function to count lines and words in a text file
def analyze_text_file(file_name):
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

#Function to write data to a CSV file
def write_to_csv(file_name):
    try:
        with open(file_name, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            print(f"\nEnter rows of data for the CSV file '{file_name}' (type 'STOP' to finish):")
            print("Separate each value with a comma (e.g., name,age,city):")

            while True:
                row = input()
                if row.strip().upper() == "STOP":
                    break
                writer.writerow(row.split(","))
        print(f"\nData has been written to the CSV file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred while writing to the CSV file: {e}")

#Function to analyze a CSV file
def analyze_csv(file_name):
    try:
        with open(file_name, "r") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            row_count = len(rows)
            cell_count = sum(len(row) for row in rows)

        return row_count, cell_count
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

#Main program
if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Create or overwrite a text file")
        print("2. Append content to a text file")
        print("3. Analyze a text file (count lines and words)")
        print("4. Create a new CSV file")
        print("5. Analyze a CSV file (count rows and cells)")
        print("6. Exit")
        choice = input("\nEnter your choice (1-6): ").strip()

#Option 1: Name of text file to be written
        if choice == "1":
            file_name = input("\nEnter the name of the text file to create or overwrite: ").strip()
            write_to_text_file(file_name, mode="w")

#Option 2: Name of text file to append content
        elif choice == "2":
            file_name = input("\nEnter the name of the text file to append content: ").strip()
            write_to_text_file(file_name, mode="a")

#Option 3: Name of text file to be analyzed
        elif choice == "3":
            file_name = input("\nEnter the name of the text file to analyze: ").strip()
            lines, words = analyze_text_file(file_name)
            if lines is not None and words is not None:
                print(f"\nText File Analysis of '{file_name}':")
                print(f"Total Lines: {lines}")
                print(f"Total Words: {words}")

#Option 4: Name of CSV file to be created
        elif choice == "4":
            file_name = input("\nEnter the name of the CSV file to create: ").strip()
            write_to_csv(file_name)

#Option 5: Name of csv file to be analyzed
        elif choice == "5":
            file_name = input("\nEnter the name of the CSV file to analyze: ").strip()
            rows, cells = analyze_csv(file_name)
            if rows is not None and cells is not None:
                print(f"\nCSV File Analysis of '{file_name}':")
                print(f"Total Rows: {rows}")
                print(f"Total Cells: {cells}")

#Option 6: Exiting the program
        elif choice == "6":
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")
