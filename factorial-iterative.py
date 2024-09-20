# The University of Law
# A simple iterative-based factorial calculator
# Dr Paul Sant
# 5 December 2023
def factorial(nterms):    
    result = 1 # must set the result = to 1 in order to ensure we do not multiply be zero on first iteration

    while nterms != 0:
        result = result*nterms # we calculate the intermediate resulrs by taking the current result and multiplying by teh next number in the sequence
        nterms = nterms-1 # reduce the loop counter by 1 for next iteration
    print(f"The factorial is {result}") # print out the result


nterms = int(input("Which term do you wish to calculate the factorial of?"))
factorial(nterms)