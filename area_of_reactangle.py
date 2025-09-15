# Class for Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Example usage
l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))

rect = Rectangle(l, w)
print(f"Area of rectangle = {rect.area()}")
