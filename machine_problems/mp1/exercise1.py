"""
PROBLEM DESCRIPTION:
- Write a program that asks the user to enter the width and length of a room.
- Once the values have been read, your program should compute and display
the area of the room.
- The length and the width will be entered as int numbers.
- Include units in your prompt and output message; either feet or meters,
depending on which unit you are more comfortable working with.

Variables:
width
length

Input:
Please enter the width of the room: 7
Please enter the length of the room: 8

Output:
The area of the room is 56m.
---
Input
Please enter the width of the room: 12
Please enter the length of the room: 23

Output
The area of the room is 276m.
"""

# Get dimensions of room
width = int(input("Please enter the width of the room in meters: "))
length = int(input("Please enter the length of the room in meters: "))

# Area formula for rectangle
area = width * length

# Display output
print("The area of the room is ", width * length, 'm.', sep='')
# print("The area of the room is {}m.".format(area))
# print(f"The area of the room is {area}m.")
