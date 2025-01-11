## Day 5: Functions

#Project: Write a function to calculate the factorial of a number

#A program to demonstrate how to define functions, use arguments, return values, and handle edge cases.

#Step 1: Define the factorial function
def factorial(num):

#Step 2: Handle invalid input (negative numbers)
    if num < 0:
        return "Factorial is not defined for negative numbers."

#Step 3: Handle the special case where number is 0
    elif num == 0:
        return 1   #0! =1 by definition

#Step 4: Calculate factorial for positive values
    else:
#Initialize result to 1
        result = 1  
#Loop from 1 to the input value (inclusive)
        for i in range(1, num + 1):  
#Multiply result by the current number in the loop
            result *= i  
#Return the final calculated factorial
        return result  

#Step 5: Get input from the user
num = int(input("Enter a number to calculate its factorial:  "))  

#Step 6: Call the factorial function and display the result
print(f"The factorial of {num} is {factorial(num)}.")