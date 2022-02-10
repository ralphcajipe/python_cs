# Nonlocal variable

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    # inner() function call and a print statement
    inner()
    print("outer:", x)


outer()