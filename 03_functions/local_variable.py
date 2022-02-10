# Local Variable
def foo():
    y = "local"
    print(y)

foo()  # Prints "local"
print(y) # NameError

"""
A variable declared inside the function's body or in the local 
scope is known as a local variable.

The output shows an error because we are 
trying to access a local variable y in a 
global scope (line 6) whereas the local variable 
only works inside foo() or local scope.
"""
