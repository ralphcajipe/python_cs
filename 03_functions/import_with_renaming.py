# Import with renaming the module
import math as m

print("The value of pi is", m.pi)

"""
We have renamed the math module as m. This can save us typing time in 
some cases.

Note that the name math is not recognized in our scope. Hence, math.pi is 
invalid, and m.pi is the correct implementation.
"""