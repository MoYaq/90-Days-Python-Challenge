#Day Two: Variables and Data Types
#Project: Create a program that takes user input for their name and age, then prints a greeting with their name and calculates the year they were born.
#A program to demonstrate the use of variable, data types and type casting (converting between types).

#Taking inputs of user’s name and age
name = input("Please enter your name:    ")
age = input("Please enter your age:   ")
Age = int(age) #turning age into an integer

#Calculating user's year of birth 
#Birthdate = BD
BD = 2025 - Age

#Printing user's information
print(f"Hi, {name}")
print(f"You are {Age} years old and you were born on the {BD}")
