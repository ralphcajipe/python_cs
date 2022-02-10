def greet(name):
    """Greets to the person passed in as an argument."""
    print(f"Hello, {name}. Good morning!")


# Function call
print(greet("Ralph"))

"""
OUTPUT:
Hello, Ralph. Good morning!
None

NOTE:
Here, None is the returned value 
since greet() directly prints the name 
and no return statement is used.
"""
