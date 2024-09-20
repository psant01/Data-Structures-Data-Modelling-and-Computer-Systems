# A simple algorithm to add up the numbers from 1-20
# This algorithm runs a loop using the number from 1 to 20
# We declare a variable called result at the beginning of the program
# Each time around the loop we add the current value i to the result
# Once the loop has completed we print out the final value of result, which is the sum
# of the number from 1 to 20.

# Code produced by: Dr Paul Sant
# Module: Data Structures, Data Modelling and Computer Systems
# Date: 19th June 2024
# Version: 1

# Setting up a variable called result

result = 0

# Loop that runs from 1 to 20, each time i takes on the next value, 1,2,3..,20

for i in range(1,21):
    result = result + i # adding the current value of i to our running total

# Print out the final result
print("The result of summing up the numbers from 1 to 20 is: ", result)