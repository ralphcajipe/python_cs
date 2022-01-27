"""
Acreage is the area of a land in acres. To calculate the acreage,
the length and width of the land, which is usually given in feet,
is multiplied to get the area in square feet.
Then, this area in square feet is converted to acres by using the
conversion factor of 43560.
Accordingly, the calculated area is divided by the conversion factor
because 1 acre = 43,560 square feet.
"""

# Variables and Input
width = int(input("Please enter the width of the field in feet: "))
length = int(input("Please enter the length of the field in feet: "))

# Area of a rectangle
area = width * length

# 1 acre = 43,560 square feet
sqFeetPerAcre = 43560

# Acreage formula
acreage = area / sqFeetPerAcre

# Display acres output
print("The area of the field in acres is", acreage, 'acres.')
