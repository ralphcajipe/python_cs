# Program to double each item in a list using map()
# The map() function in Python takes in a function and a list.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(map(lambda x: x * 2, my_list))

print(new_list)

"""
The function is called with all the items in the list and a new
list is returned which contains items returned by that function
for each item.
"""
