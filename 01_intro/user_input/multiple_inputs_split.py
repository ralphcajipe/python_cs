# Taking Multiple Inputs From User Using split() Method

"""
A programmer often wants a user to enter multiple values or inputs
in one line. In Python user can take multiple values or inputs in
one line by two methods.

- Using split() method
- Using List comprehension

In this file, I'll use split() method.

Using split() method :
This function helps in getting multiple inputs from users.
It breaks the given input by the specified separator.
If a separator is not provided then any white space is a separator.
Generally, users use a split() method to split a Python string
but one can use it in taking multiple inputs.

Syntax :

input().split(separator, maxsplit)
"""

"""
# taking two inputs at a time
# example: 25 99
x, y = input("Enter two values: ").split()
print(x)
print(y)
print()

# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print(x)
print(y)
print(z)
print()

# taking two inputs at a time using f-strings
a, b = input("Enter two values: ").split()
print(f"First number is {a} and second number is {b}.")
print()
"""

# taking two inputs at a time using .format() method
a, b = input("Enter two values: ").split()
print("First value is {} and second value is {}".format(a, b))

# taking multiple inputs at a time
# and type casting using list() function
numbers = list(map(int, input("Enter multiple values: ").split()))
print(numbers)
