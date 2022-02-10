# Recursion
# factorial problem
# 4!
# 4 X 3 X 2 X 1 = 24


def factorial(n):
    """Get the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Input a number "))
print(factorial(n))
