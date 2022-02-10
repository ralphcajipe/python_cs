# Program to filter out only the even items from a list.
# The filter() function in Python takes in a function and a list as
# arguments.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(filter(lambda x: x % 2 == 0, my_list))

print(new_list)

"""
The function is called with all the items in the list and a new 
list is returned which contains items for which the function 
evaluates to True.
"""
