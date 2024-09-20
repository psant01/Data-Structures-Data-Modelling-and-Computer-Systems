# The University of Law
# Software development module
# A simple program to sort numbers into order from smallest to largest

# Get three numbers from the user
num1 = int(input("Please enter your first number:"))
num2 = int(input("Please enter your second number:"))
num3 = int(input("Please enter your third number:"))

if num1 > num2:
    # swap the order of num1 and num 2
    temp = num1
    num1 = num2
    num2 = temp
if num1 > num3:
    # swap the order of num1 and num3
    temp = num1
    num1 = num3
    num3 = temp
if num2 > num3:
    #swap the order of num2 and num3
    temp = num2
    num2 = num3
    num3 = temp
else:
    print("The numbers are already in order.")
print(f"The smallest number is {num1}, the next smallest number is {num2} and the largest number is {num3}")


