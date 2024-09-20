# The University of Law
# Software Development Module
# Example of recursion - Factorial
# The factorial of a number is given as multiplying all numbers
# in a sequence together
# Example (Factorial(4)) = 4 x 3 x 2 x 1 = 24
# Factorial (1) is 1 (and is our base case to stop the recusion)

def factorial(n):
    if n <= 0:
        print("Error")
    elif n == 1:
        return 1 # this is our base case and will stop the recursion
    else:
        return(n*factorial(n-1))

# Now we are going to test our factorial function by asking the user for input


nterms = int(input("Which number do you wish to calculate the Factorial of?"))
result = factorial(nterms) # call the factorial function and store the result is variable result

print(f"The Factorial of {nterms} is {result}")