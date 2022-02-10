def my_function():
    """Local scope of variable x."""
    x = 10
    print("Value of x inside a function:", x)


# Global scope of variable x.
x = 20

my_function()
print("Value of x outside a function:", x)