"""
NOTE: When encountering division with % modulo and
// floor, the order of operations is divide from left to right.
"""
a = 16
b = 15

num = a % b // a

print(num)
"""
Correct if a % b first:
>>> 16 % 15
1
>>> 1 // 16
0
Output: 0

Incorrect if b // a:
>>> 15 // 16
0
>>> 16 % 0
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    16 % 0
ZeroDivisionError: integer division or modulo by zero
"""
