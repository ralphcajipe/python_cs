"""
The output of the print() function always ends by a newline
character. The print() function has another optional
parameter end, whose default value is "\n". This value can be
substituted by any other character such as a single space (' ')
to display the output of the next print() statement in
the same line. This is especially useful in a Python script like
the one shown below:
"""

name = "ralph"
age = 21

print("Name:", name, end=' ')
print("Age:", age)

"""
It is possible to format the output using C style format specifier symbols 
such as %d for integer, %f for floar, %s for string etc.
"""
