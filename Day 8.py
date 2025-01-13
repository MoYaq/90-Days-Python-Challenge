#Day 8: File I/O
#Project: Read a text file and count the number of lines and words.

#Step 1: Import necessary modules
#No external modules are required for this basic implementation.

#Step 2: Function to count lines and words
def count_lines_and_words(file_name):
    try:
#Open the file in read mode using 'with' (ensures automatic file closure)
        with open(file_name, "r") as file:
            content = file.readlines()  # Read all lines into a list

#Count lines
        line_count = len(content)

#Count words
        word_count = sum(len(line.split()) for line in content)

        return line_count, word_count

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


#Step 3: Main Program
if __name__ == "__main__":
#Prompt user for the file name
    file_name = input("Enter the name of the text file (with extension, e.g., 'example.txt'): ").strip()

#Count lines and words in the specified file
    lines, words = count_lines_and_words(file_name)

#Display the results
    if lines is not None and words is not None:
        print(f"\nFile Analysis:")
        print(f"Total Lines: {lines}")
        print(f"Total Words: {words}")