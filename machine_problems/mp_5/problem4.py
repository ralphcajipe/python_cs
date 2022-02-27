"""
Machine Problem 4:
Generate the following output using the following letters:
abcdefghijklmnopqrstuvwxyz

Multiply each letter, starting with letter 'a', incrementally/increasing
- e.g., 'a' == 'a'
'b' == 'bb'
'c' == 'ccc'
'd' == 'dddd' and so on...
"""

letters = "abcdefghijklmnopqrstuvwxyz"

list_of_letters = []
for letter in letters:
    list_of_letters.append(letter)
# print(list_of_letters)

multiplied_letters = []
multiplier = 1
for letter in list_of_letters:
    letter *= multiplier
    multiplier += 1
    multiplied_letters.append(letter)
print("OUTPUT IS", multiplied_letters)
