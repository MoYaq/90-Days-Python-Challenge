#Day 6: Lists and Tuples

#Project: Create a program that takes a list of numbers and prints the sum and average.

#A program to demonstrate how to create, access, modify, and delete elements using list methods: append(), remove(), pop().


#Step 1: Initialize an empty list to store user input
numbers = []

#Prompt the user to enter numbers
print("Enter numbers for the list (press Enter to \nfinish):")

#Contiually ask for input, until they press "ENTER" to break/stop.
while True:
    user_input = input("Enter a number: ")
    if user_input == "":  #If the user presses enter (empty input)
            break  #Exit the loop
    else:
        try:
            num = int(user_input) #Try to convert input to integer
            numbers.append(num) #Add the number to the list
            space_count = 0 #Reset space count when valid input is given
        except ValueError:
            print("Please enter a valid number or press the Enter to finish.")

#Print the list of numbers entered by the user
print("\nList of numbers entered:")
print(numbers)

#Step2: Allow the user to perform different actions
while True:
    print("\nWhat would you like to do next?")
    print("\n1. Add a number to the list")
    print("2. Remove a specific number from the list")
    print("3. View the last number from the list")
    print("4. View the list")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
#Add a number to the list
        num_to_add = int(input("Enter the number to add: "))
        numbers.append(num_to_add)
        print(f"\n{num_to_add} has been added to the list.")

    elif choice == "2":
#Remove a specific number from the list
        num_to_remove = int(input("Enter the number to remove: "))
        if num_to_remove in numbers:
            numbers.remove(num_to_remove)
            print(f"\n{num_to_remove} has been removed from the list.")
        else:
            print(f"\n{num_to_remove} is not in the list.")

    elif choice == "3":
#Pop (view) the last number from the list
        if numbers:
            last_number = numbers.pop()
            print(f"\n{last_number} is the last number in the list.")
        else:
            print("\nThe list is empty, nothing to view.")

    elif choice == "4":
#View the list
        print("\nCurrent List:")
        print(numbers)

    elif choice == "5":
#Exit the loop
        print("\nExiting the program.")
        break

    else:
        print("\nInvalid choice, please enter a number between 1 and 5.")

#Step 3: Print the final list and the sum and average
print("\nFinal List:")
print(numbers)

#Filtering out 0 to handle edge cases where its inclusion would affect the true average by improperly increasing the count of values.
filtered_numbers = [num_to_be_filtered for num_to_be_filtered in numbers if num_to_be_filtered != 0]


list_sum = sum(filtered_numbers) #Sum of non_numbers
list_count = len(filtered_numbers) #Count of non-zero numbers
list_avg = list_sum / list_count if list_count > 0 else 0 #Error Handling, to avoid division by zero if list count is equal to 0

print("Sum of non-zero numbers in the list \n=", list_sum)
print("Count of non-zero numbers in the list \n=", list_count)
print("Average of non-zero numbers in the list \n=", list_avg)


#Addendum:

#Because this program is a "sum and average" calculator, the position of the numbers doesn't matter. 
#Hence, there is no direct need to use the `insert()` method. However, for purpose of knowing how to use it, this is how it is done:

#The syntax is:
#numbers.insert(index, x)
#where:
# - `numbers` is the defined value for list where you want to insert the new element/number.
# - `index` is the position where you want to insert the element (starting from 0, the first position).
# -  `x` is the element/number you want to insert.

#The `insert()` method modifies the original list in-place, so it doesn't return a new list.
#It simply inserts the element at the specified index and shifts the elements to the right.

#The `insert()` method is useful when you want to insert an element at a specific position in a list without modifying the original list.
#It allows you to insert an element at a specific index without affecting the order of the other elements in the list.

#The `insert()` method is a commonly used method in Python programming for adding elements to a list at a specific position.
#It allows you to insert an element at a specific index without modifying the original list.

#For example:
#list = [1, 2, 3, 4, 5]
#To insert 6 at the third position (index 2):
#list.insert(2, 6)

#Results:
#list = [1, 2, 6, 3, 4, 5]