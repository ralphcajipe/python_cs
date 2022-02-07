# function accepts two args
# print the * (x)-> rows, (y) -> cols

def rectangle(m, n):
    for i in range(0, m):
        out = n * "*"
        print(out)


rectangle(6, 10)
