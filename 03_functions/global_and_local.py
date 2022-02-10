# Global and Local Variables
x = "global "


def sample():
    """Function with global and local variables."""
    global x
    x = x * 2
    y = "local"
    print(x)
    print(y)


sample()

"""
In the code, we declare x as a global and y as a 
local variable in the sample(). 

Then, we use multiplication operator * to 
modify the global variable x and we print 
both x and y.

After calling the sample(), the value 
of x becomes `global global` because we used 
the x * 2 to print global two times. After that, 
we print the value of local variable y example `local`.
"""
