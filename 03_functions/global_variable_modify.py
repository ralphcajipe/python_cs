# Modifying Global Variable From Inside the Function using global.
# Changing Global Variable From Inside a Function using global.

# global variable
number = 0

def add():
    global number
    number = number + 2  # incremet number by 2
    print("Inside add() function:", number)


add()
print("Outside or in main:", number)

"""
In the above program, we define number as a global 
keyword inside the add() function.

Then, we increment the variable number by 1, 
i.e number = number + 2. After that, we call the add() function. 

Finally, we print the global variable number.
As we can see, change also occurred on the 
global variable outside the function, number = 2.
"""
