# Global Variable

x = "global"


def sample():
    print("x inside is", x)


sample()
print("x outside is", x)

"""
In the above code, we created x as a global 
variable and defined a sample() to print the 
global variable x. 

Finally, we call the sample() which will print 
the value of x.
"""