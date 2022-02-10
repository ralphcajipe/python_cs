import config
import update

print(config.a)
print(config.b)

"""
I have created three files: config.py, update.py, and global_test_main.py.

The module config.py stores global variables of a and b. In the update.py file, 
we import the config.py module and modify the values of a and b. 
Similarly, in the global_test_main.py file, we import both config.py 
and update.py module. 

Finally, we print and test the values of global variables whether they are 
changed or not. In result, they changed because of our update.
"""