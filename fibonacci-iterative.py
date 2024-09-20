# An iterative version to calculate the nth number
# in the Fibonacci sequence
# Produced by Mandy Wong
# Original code available at: https://realpython.com/fibonacci-sequence-python/

def fibonacci_of(n):
    # Validate the value of n
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    # Handle the base cases
    if n in {0, 1}:
        return n # our base cases

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number

nterms = int(input("please enter the term in the Fibonacci sequence that you would like to calculate:"))
result = fibonacci_of(nterms) # call the fibonacci_of function
print(f"The {nterms} th number in the Fibonacci series is: {result}")