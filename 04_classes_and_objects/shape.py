class Shape:
    """Width and Height of a shape."""
    width = 0
    height = 0

    def area(self):
        print("Parent Class Area")


class Rectangle(Shape):
    """Get area of a rectangle."""

    def __init__(self, w, h):
        self.width = w
        self.height = h

    # overidding
    def area(self):
        print("Area of Rectange is", self.width * self.height)


class Triangle(Shape):
    """Get area of a triangle."""

    def __init__(self, w, h):
        self.width = w
        self.height = h

    # overidding
    def area(self):
        print("Area of Triangle is", self.width * self.height / 2)


rectangle = Rectangle(10, 20)
triangle = Triangle(2, 10)

rectangle.area()
triangle.area()
