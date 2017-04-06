# def my_reduce(num_list):
#     return reduce(num_list)

def add(num_list):
    """Return the sum of two numbers"""
    for i in num_list:
        i = float(i)
    num_list_sum = sum(list(num_list))
    return num_list_sum

def subtract(num_list):
    """Return the difference of two numbers"""
    for i in num_list:
        i = float(i)        
    for i in num_list[1:]:
        subtractors = [i * -1]
    num_list_sum = num_list[0] + sum(list(subtractors))
    return num_list_sum

def multiply(num_list):
    """Return the product of two numbers"""
    return num1 * num2

def divide(num_list):
    """Return the quotient of two numbers as a float"""
    return float(num1) / num2

def square(num_list):
    """Return the square of a number"""
    return num ** 2

def cube(num_list):
    """Return the cube of a number"""
    return num ** 3

def power(num_list):
    """Return num raised to the power of exponent"""
    return num ** exponent

def mod(num_list):
    """Return remainder of num1 divided by num2"""
    return num1 % num2
