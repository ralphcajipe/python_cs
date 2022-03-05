"""
The chdir() Method:
You can use the chdir() method to change the current
directory. The chdir() method takes an argument, which is
the name of the directory that you want to make the current
directory.

Syntax:
os.chdir("newdir")

Example:
import os
os.chdir("/home/newdir")

"""

import os

# Move to new_dir directory
os.chdir("..\\home\\my_dir")

current_directory = os.getcwd()
print(current_directory)
