#Day 9: Error Handling
#Project: A program that takes user input for a number and catches errors if the input is invalid (non-integer).
#A program to demonstrate how to handle errors in Python using try, except, and finally blocks.

#Step 1: Prompt the user to input a number.
def get_number():
    while True:
        try:
#Ask the user for input
            user_input = input("\nEnter a number to confirm if it is an integer: \n").strip()

#Step 2: Attempt to convert the input to an integer
            number = int(user_input)

#If successful, return the number
            print(f"{number} is an integer")
            return number

        except ValueError:
#Step 3: Handle the case where input cannot be converted to an integer
            if "." in user_input:
                print("Invalid input! It seems you entered a decimal number. Please enter an integer.")
            elif user_input.isalpha():
                print("Invalid input! It seems you entered letters. Please enter an integer.")
            else:
                print("Invalid input! Please enter a valid integer number.")

#Optional: A message that always runs after the try-except (just to demonstrate how to use a finally block)
        finally:
            print("Attempt completed. Try again if necessary.")

#Main Program
if __name__ == "__main__":
    print("Welcome to the Integer Checker!")

#Call the function to get a number
    get_number()

    print("Thank you for using the program. Feel Ya 😂!")
