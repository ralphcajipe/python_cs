# Program to show the use of lambda function

double = lambda x: x * 2

print(double(2))

"""
NOTE:
In the above program, lambda x: x * 2 is the lambda function. 
Here, x is the argument and x * 2 is the expression that gets evaluated 
and returned. This function has no name. It returns a function object which is
assigned to the identifier double. We can now call it as a normal function. 
The statement double = lambda x: x * 2 is nearly the same as: 
def double(x): return x * 2
"""
