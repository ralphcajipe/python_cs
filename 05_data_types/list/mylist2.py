mylist = [1, 2, 3, 4, 4, 4, 5, 5, 'a', 'b']

# 1 count the number of occurance of the number 4
# count()
print(mylist.count(4))
print(mylist.count('a'))

# 2. remove items
# 2.1 remove last item -> pop()
print('popped value', mylist.pop())
print(mylist)

# mylist =
# 3 -> append method
mylist = ['a', 'b', 'c', 'd', 'e']
mylist.append(1)
print(mylist)

myotherlist = [1, 2, 3, 4]

# #4 strings
mylist = list("ralph")
print(mylist)

# #reverse
mylist.reverse()
print(mylist)

# sort
mylist = ['x', 'e', 'm', 'p', 'a']
mylist.sort()
print(mylist)

mylist2 = [6, 3, 9, 1, 0]
mylist2.sort()
print(mylist2)
