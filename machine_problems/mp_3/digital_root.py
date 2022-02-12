def digital_root(num):
    """Function that gets the digital root of any number."""
    if len(num) == 1:
        return num
    else:
        the_sum = 0
        for i in num:
            the_sum += int(i)
        num = str(the_sum)
        return digital_root(num)


my_num = input("Enter the number:")

print("The digital root of is:", digital_root(my_num))
