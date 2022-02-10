# Global variable and Local variable with the same name
x = 5

def sample():
    x = 10
    print("local x is", x)


sample()
print("global x is", x)

"""
In the above code, we used the same name x for both global 
variable and local variable. 

We get a different result when we print the same variable 
because the variable is declared in both scopes, i.e. the local 
scope inside sample() and global scope outside sample().

When we print the variable inside sample() it outputs local x: 
10. This is called the local scope of the variable.

Similarly, when we print the variable outside the sample(), it 
outputs global x: 5. This is called the global scope of the 
variable.
"""