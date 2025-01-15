#Day 10: Introduction to Libraries
#Project: Create a program to calculate the square root of a number using the math library.
#A project to demonstrate how to use in-built Python libraries like math

#Step 1: Importing the math library
import math

#Step 2: Define a function to calculate the square root
def calculate_square_root():
    while True:
        try:
#Step 3: Prompt the user to input a number
            user_input = input("\nEnter a number to find its square root (or type 'exit' to quit): ").strip()

#Allow the user to exit the program
            if user_input.lower() == 'exit':
                print("\nExiting the program. Byyyye....!")
                break

#Convert the input to a float
            number = float(user_input)

#Check if the number is non-negative
            if number < 0:
                print("Error: Square root of a negative number is not defined for real numbers.")
            else:
#Calculate and display the square root (leaving results in 3 decimal place)
                square_root = math.sqrt(number)
                print(f"The square root of {number} is {square_root:.3f}.")
        except ValueError:
#Handle invalid input
            print("Invalid input! Please enter a valid number.")

#Main program
if __name__ == "__main__":
    print("Square Root Calculator!")
    print("\nThis program uses the built-in math library to calculate square roots.")
    calculate_square_root()
