# Global in Nested Functions
def outer():
    x = 20

    def inner():
        global x
        x = 25

    print("Beffore calling inner:", x)
    print("Calling inner now")
    inner()
    print("After calling inner:", x)


outer()
print("x in main: ", x)

"""
In the above program, we declared a global variable 
inside the nested function inner(). 

Inside sample() function, x has no effect of the global 
keyword.

Before and after calling inner(), the variable x takes the 
value of local variable example x = 20. 

Outside of the sample() function, the variable x will take 
value defined in the inner() function example x = 25. This is 
because we have used global keyword in x to create 
global variable inside the inner() function (local scope).

If we make any changes inside the inner() function, the 
changes appear outside the local scope, 
example sample().
"""