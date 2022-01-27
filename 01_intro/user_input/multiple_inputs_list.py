# # Taking Multiple Inputs From User Using List Comprehension

"""
Using List comprehension :
List comprehension is an elegant way to define
and create list in Python.
We can create lists just like mathematical statements in one line only.

NOTE:
    It is also used in getting multiple inputs from a user.
"""

"""
# taking two input at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print(x)
print(y)
print()
"""

"""
# taking three input at a time
x, y, z = [int(x) for x in input("Enter three values: ").split()]
print(x)
print(y)
print(z)
"""

"""
# taking two input at a time using .format() method
x, y = [int(x) for x in input("Enter two values: ").split()]
print("{} and {}".format(x, y))
"""

"""
# taking multiple inputs at a time
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Numbers of list: ", x)
"""

"""
Note: 
    The above examples take input separated by spaces. 
    In case we wish to take input separated by comma (, ), 
    we can use the following: 
"""
# taking multiple inputs at a time separated by comma
print("You can enter multiple inputs separated by coma.\n\
Example: 1,2,3,4,5")

x = [int(x) for x in input("Enter multiple values: ").split(",")]
print("Numbers of lists: ", x)
