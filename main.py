import sys
import os

#Vars
numbers = []
count = 1

#Get numbers from user
print("Enter your numbers. Enter stop in order to start calculating.")
while True:
    appendNumber = input("Enter number " + str(count) + ": ")
    if appendNumber == ("stop"):
        break;
    appendNumber = int(appendNumber)
    count = count+1
    numbers.append(appendNumber)
    
#Calulate median
if len(numbers) % 2 == 1:
    numbers.sort
    numbersIndex = int(len(numbers)/2)
    print("The median of the numbers is " + str(numbers[numbersIndex]))
elif len(numbers) % 2 == 0:
    numbers.sort
    numbersIndex = int(len(numbers)/2 - 1)
    numbersIndex2 = int((len(numbers)+2)/2 - 1)
    finalMedian = ((numbers[numbersIndex] + numbers[numbersIndex2]) /2)
    #Output median
    print("The median of the numbers is " + str(finalMedian))
    
#Output average
print("The average of the numbers is " + str((sum(numbers))/(len(numbers))))

returnAgain = input("Do you want to rerun the program? (Y/N) ")
if returnAgain == "Y":
    os.execl(sys.executable, sys.executable, * sys.argv)
