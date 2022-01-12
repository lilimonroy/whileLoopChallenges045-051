#----------* CHALLENGE 47 *----------
#Ask the user to enter a number and then enter another number. Add these two numbers together and
# then ask if they want to add another number. If they enter “y", ask them to enter another number and keep 
# adding numbers until they do not answer “y”. Once the loop has stopped, display the total.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

total = num1 + num2

answer = input("Do yo want to add another number: [y|n] ")

while answer == 'y':
    num3 = int(input("Enter a number again: "))
    total = total + num3
    answer = input("Do yo want to add another number: [y|n] ")

print("The total is",total)

