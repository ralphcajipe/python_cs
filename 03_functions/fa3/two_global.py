x = 100


def f1():
    global x

    x = 90


def f2():
    global x

    x = 80

print(f1())
print(f2())
print(x)
