my_list = []


def convert(b):
    """Gives the binary equivalent of the number."""
    if (b == 0):
        return my_list

    dig = b % 2
    my_list.append(dig)
    convert(b // 2)


convert(6)
my_list.reverse()

for i in my_list:
    print(i, end="")
