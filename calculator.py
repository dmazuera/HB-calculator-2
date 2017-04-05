"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

while True:
    input = raw_input()
    tokenized_input = input.split(" ")
    if tokenized_input[0] == "q" or tokenized_input[0] == "quit":
        #this will exit calculator
        break
    elif tokenized_input[0] == "+":
        #arithmetic add function
        print add(float(tokenized_input[1]), float(tokenized_input[2]))
    elif tokenized_input[0] == "-":
        #arithmetic subtract function
        print subtract(float(tokenized_input[1]), float(tokenized_input[2]))
    elif tokenized_input[0] == "*":
        #arithmetic multiply function
        print multiply(float(tokenized_input[1]), float(tokenized_input[2]))
    elif tokenized_input[0] == "/":
        #arithmetic divide function
        print divide(float(tokenized_input[1]), float(tokenized_input[2]))
    elif tokenized_input[0] == "square":
        #arithmetic square function
        print square(float(tokenized_input[1]))
    elif tokenized_input[0] == "cube":
        #arithmetic cube function
        print cube(float(tokenized_input[1]))
    elif tokenized_input[0] == "pow":
        #arithmetic power function
        print power(float(tokenized_input[1]), float(tokenized_input[2]))
    elif tokenized_input[0] == "mod":
        #arithmetic modulo function
        print mod(float(tokenized_input[1]), float(tokenized_input[2]))
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