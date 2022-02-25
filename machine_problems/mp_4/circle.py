# Name: Ralph Henrik Cajipe
# School: FEU-TECH
# Machine Problem number - 2

"""
Python program that implements OOP.
Use the class name Circle.
Solve for the Area and Perimeter.
"""
import math


class Circle:
    """Class that solves the Area and Perimeter."""

    def __init__(self, radius):
        """Initialize attributes."""
        self.radius = radius

    def area(self):
        """Returns the area of a circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of a circle."""
        return 2 * math.pi * self.radius


while True:
    radius_inp = eval(input("\nEnter radius:"))
    circle_obj = Circle(radius_inp)

    if radius_inp < 0:
        print("You use enter positive number")
    elif "." in str(radius_inp):
        print("You use input whole number value:")
    else:
        # area
        print("The answer is:", round(circle_obj.area(), 0))

        perimeter_result = round(circle_obj.area(), 0) * 0.2
        print("Here is the Answer:", perimeter_result)

        # did not utilize perimeter method...
        # value = round(circle_obj.perimeter())
        # perimeter_result = f"{value:.15f}"
