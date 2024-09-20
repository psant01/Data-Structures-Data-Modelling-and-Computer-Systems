# The University of Law

# Classwork - a simple program that demonstrates the beauty of recursion

def fibonacci(n):
    #if the number is one or two then the result is 1

    if n<=1:
        return 1
    else:
        # Othwerise the result is the sum of the previous two numbers in the sequence
        return (fibonacci(n-1) + fibonacci(n-2))
    
nterms=0
nterms = int(input("Which Finobacci number in the sequence would you like?"))
result = fibonacci(nterms)

print(f"The {nterms}th number in the fibonacci sequence is {result}")


