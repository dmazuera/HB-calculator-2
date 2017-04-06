"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here


while True:
    input = raw_input()
    tokenized_input = input.split(" ")

    num1 = float(tokenized_input[1])
    # try:
    #     tokenized_input[2]
    #     num2 = float(tokenized_input[2])
    # except:
    #     pass

    floated_input = [float(x) for x in tokenized_input[1:]]

    if tokenized_input[0] == "q" or tokenized_input[0] == "quit":
        #this will exit calculator
        break
    elif tokenized_input[0] == "+":
        #arithmetic add function
        print add(num1, num2)
    elif tokenized_input[0] == "-":
        #arithmetic subtract function
        print subtract(num1, num2)
    elif tokenized_input[0] == "*":
        #arithmetic multiply function
        print multiply(num1, num2)
    elif tokenized_input[0] == "/":
        #arithmetic divide function
        print divide(num1, num2)
    elif tokenized_input[0] == "square":
        #arithmetic square function
        print square(num1)
    elif tokenized_input[0] == "cube":
        #arithmetic cube function
        print cube(num1)
    elif tokenized_input[0] == "pow":
        #arithmetic power function
        print power(num1, num2)
    elif tokenized_input[0] == "mod":
        #arithmetic modulo function
        print mod(num1, num2)
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