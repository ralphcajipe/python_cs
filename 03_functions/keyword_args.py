def greet(name, message="Good morning!"):
    """Greets to the person with the message.
    If the message is not provided,
    it defaults to "Good morning!"
    """

    print(f"Hello {name}, {message}")


# 2 keyword arguments
greet(name="Ralph", message="how do you do?")

# 2 keyword arguments (out of order)
greet(message="how do you do?", name="Ralph")

# 1 positional, 1 keyword argument
greet("Bruce Wayne", message="what's the plan?")

"""
NOTE:
Having a positional argument after keyword arguments will result 
in errors. For example, the function call as follows:

greet(name="Ralph","how do you do?")

Will result in an error:
SyntaxError: non-keyword arg after keyword arg
"""
