#Day Two
#Program to greet and tell users their birthdate


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