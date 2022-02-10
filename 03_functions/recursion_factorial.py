def factorial(num):
    """Recurisve function to find the factorial of a number."""

    if num == 1:
        return 1  # return True
    else:
        return num * factorial(num - 1)


my_num = 3
print(f"The factorial of {my_num} is {factorial(my_num)}")

"""
NOTE:
In the example, factorial() is a recursive function as it calls itself.
When we call this function with a positive integer, 
it will recursively call itself by decreasing the number.

step-by-step process of Recursion:
1. Our recursion ends when the number reduces to 1. This is 
called the base condition.

2. Every recursive function must have a base condition that stops 
the recursion or else the function calls itself infinitely.

3. The Python interpreter limits the depths of recursion to help 
avoid infinite recursions, resulting in stack overflows.

4. By default, the maximum depth of recursion is 1000.
"""
