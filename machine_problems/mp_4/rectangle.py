"""
Program that implements OOP.
Use the class named Rectangle to compute the Area of a rectangle.
The class must pass two arguments to compute for the area of a rectangle.
"""


class Rectangle:
    """Class to compute the Area of a Rectangle."""

    def __init__(self, length, width):
        """Initialize attributes."""
        self.length = length
        self.width = width

    def area(self):
        """Formula for Area"""
        return self.length * self.width


print("Enter 'quit()' when you want to exit.")
while True:
    try:
        length_inp = eval(input("\nEnter Length value:"))
        width_inp = eval(input("Input the width of the rectangle:"))
    except NameError:
        print("\tPlease enter numbers for computation.")

    else:
        # area object instance
        area_obj = Rectangle(length_inp, width_inp)

        if length_inp and width_inp < 0:
            print("The number is not a positives integer:")

        # if length and width are both float
        elif "." in str(length_inp) and str(width_inp):
            print("Input the correct data format is not a Positive integer:")

        else:
            print("The Area of the Rectangle is:", area_obj.area())
