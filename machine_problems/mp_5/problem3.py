"""
Machine Problem 3:
Given the following list of numbers:
    Replace all the entries in the list
    that are greater than 10 with n.
"""

data = [30, 7, 30, 2, 88, 44, 60, 40, 1, 53, 100, 72, 86, 64,
        40, 85, 3, 19, 63, 84, 17, 31, 95, 84, 99, 60, 85, 74,
        65, 38, 43, 80, 39, 70, 8, 21, 32, 68, 64, 155, 88, 84,
        49, 68, 70, 98, 21, 51, 3, 97]

equal_values, not_equal_values = 0, 0

for number in range(len(data)):
    if data[number] > 10:
        data[number] = 666
        equal_values += 1
    else:
        not_equal_values += 1

print("OUTPUT is", data)
print("Total equal values", equal_values)
print("Total not equal values", not_equal_values)
