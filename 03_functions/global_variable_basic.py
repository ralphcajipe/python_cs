# Use of global variable without the global keyword
number = 1

def add():
    print(number)


add()

"""
However, we may have some scenarios where we
need to modify the global variable from inside a function.

This is because we can only access the 
global variable but cannot modify it 
from inside the function.

The solution for this is to use 
the global keyword. See `global_variable_modify.py`.
"""