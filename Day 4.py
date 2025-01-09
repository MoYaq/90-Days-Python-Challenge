#Day Four
#Building a simple "countdown" program
#A program to demonstrate the use of both while loops and for loops.

#1.Using a while loop for the countdown
print("Countdown using a while loop:")

count = 10  #Initialize the starting number
while count > 0:  #Loop until count is greater than 0
    print(count)  #Print the current count
    count -= 1  #Decrease count by 1
    
print("Hurray While Loop Countdown Complete") #Message after while loop countdown

#2. Using a for loop for the countdown
print("Countdown using a for loop:")

for count in range(10, 0, -1):  #Start at 10, go to 1, decrement by 1
    print(count)  #Print the current count

print("Hurray For Loop Countdown Complete") #Message after for loop countdown
