#Day Three: Conditional Statements
#Project: Building a simple "age-eligibility/qualification checker"
#A program to demonstrate the using if, elif, and else statements.

#1.a) Ask the user for their name
name = input("Please, what is your name? ")

#1.b) Ask the user for their age
age = int(input(f"{name}! Please enter your age: "))

#2. Check qualification for senior session (minimum age 21)
if age >= 21: #If the age is 21 or older, the person is qualified for the senior session
    print(f"Congratulations, {name}! You are qualified for the senior session of Moyaq CodersHub boot camp.")

#3. Check qualification for junior session (minimum age 16, but less than 21)
elif age >= 16 and age < 21:  # If the age is between 16 and 20, they are qualified for the junior session
    print(f"{name}, you are qualified for the junior session of the Moyaq CodersHub bootcamp.")


else:#If the age is below 16, they are not qualified for the boot camp
    years_left= 16 - age  #Calculate the years left to be qualified for the bootcamp
    if years_left == 1:
        print(f"Sorry, {name}. You are not qualified for the Moyaq CodersHub bootcamp.")
        print(f"Kiddo! Come back when you are {years_left} year older. But for now, just concentrate on your Pokémon and cartoons😂💔")
    else:
        print(f"Sorry, {name}. You are not qualified for the Moyaq CodersHub bootcamp.")
        print(f"Kiddo! Come back when you are {years_left} years older. But for now, just concentrate on your Pokémon and cartoons😂💔")
