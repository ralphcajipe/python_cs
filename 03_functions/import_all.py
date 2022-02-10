# Import all names

"""
We can import all names(definitions) from a module
using the following construct:
from module import *

Here, we have imported all the definitions from the math module.
This includes all names visible in our scope except those beginning with
an underscore(private definitions).
"""

from math import *

# pi = "to confuse the pi method"
print("The value of pi is", pi)

"""
WARNING:
Importing everything with the asterisk (*) symbol is NOT a good 
programming practice. This can lead to duplicate definitions for an 
identifier. It also hampers the readability of our code.
"""
