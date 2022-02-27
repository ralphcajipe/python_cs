my_data = (1, [9, 8, 7], "World")
# my_data = [1,[9,8,7],"World"]
print(my_data)

# error  TypeError: 'tuple' object does not support item assignment
# my_data[0]=100
# print (my_data)

my_data[1][2] = 99
print(my_data)
