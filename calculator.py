"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here


while True:
    input = raw_input()
    tokenized_input = input.split(" ")


    try:
        tokenized_input[1:]
        num_list = [float(x) for x in tokenized_input[1:]] #num_list does not include operator
    except:
        pass


    if tokenized_input[0] == "q" or tokenized_input[0] == "quit":
        #this will exit calculator
        break

    elif tokenized_input[0] == "+":
        #arithmetic add function - takes lists
        print add(num_list)
    elif tokenized_input[0] == "-":
        #arithmetic subtract function - given list, will subtract 
        #all other numbers from the first number
        print subtract(num_list)
    elif tokenized_input[0] == "*":
        #arithmetic multiply function - takes lists
        print multiply(num_list)



    elif tokenized_input[0] == "/":
        #arithmetic divide function - only 2 numbers
        print divide(num_list[1], num_list[2])
    elif tokenized_input[0] == "square":
        #arithmetic square function - takes single num input
        print square(num_list[1])
    elif tokenized_input[0] == "cube":
        #arithmetic cube function - takes single num input
        print cube(num_list[1])
    elif tokenized_input[0] == "pow":
        #arithmetic power function - input base, exponent
        print power(num_list[1], num_list[2])
    elif tokenized_input[0] == "mod":
        #arithmetic modulo function - input dividee and divisor
        print mod(num_list[1], num_list[2])
    else:
        print "I do not understand!"


# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token