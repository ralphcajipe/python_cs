def greet(*names):
    """Greets all the persons in the names tuple."""

    # `names` is a tuple with arguments.
    for name in names:
        print("Hello", name)


# Here, we have called the function with multiple arguments.
greet("Ralph", "Elon", "Sundar", "Bill")

"""
NOTE:
These arguments get wrapped up into an immutable object called
tuple () before being passed into the function. 

Inside the function, we use a for loop to 
retrieve all the arguments back.
"""
