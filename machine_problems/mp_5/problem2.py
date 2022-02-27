"""
Machine Problem 2:
Given the following list of numbers 18,19,20
    Do the following a,b,c,d,e, and f.
"""

l = [18, 19, 20]
print("Original list", l)

# (a) Set the second entry (index 1) to 17
l[1] = 17
print("a", l)

# (b) Add 4, 5, and 6 to the end of the list
l.extend([4, 5, 6])
print("b", l)

# (c) Remove the first entry from the list
l.pop(0)
print("c", l)

# (d) Sort the list
l.sort()
print("d", l)

# (e) Double the list
l.extend(l)
print("e", l)

# (f) Insert 25 at index 3
l[3] = 25
print("f", l)
