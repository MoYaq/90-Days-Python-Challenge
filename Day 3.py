# Day 3
## Building a simple "eligibility checker"
# A program to ask for users' ages and determine their eligibility for a certain session of YaqCodeHub boot camp.
# Things to learn: Using if, Elif, and else statements

#1.a) Ask the user for their name
name = input("What is your name? ")

#1.b) Ask the user for their age
age = int(input(f"Hello, {name}! Please enter your age: "))

#2. Check eligibility for senior session (minimum age 21)

if age >= 21: #If the age is 21 or older, the person is eligible for the senior session
    print(f"Congratulations, {name}! You are eligible for the senior session of Moyaq CodersHub boot camp.")

    # Check eligibility for junior session (minimum age 16, but less than 21)
elif age >= 16 and age < 21:  # If the age is between 16 and 20, they are eligible for the junior session
    print(f"{name}, you are eligible for the junior session of Moyaq CodersHub bootcamp.")

else: #If the age is below 16, they are ineligible for the boot camp
    print(f"Sorry, {name}. You are not eligible for the Moyaq CodersHub bootcamp.")
    print(f"Please come back when you are {16 - age} years older. But for now just concentrate on your Pokemon and cartoons😂")