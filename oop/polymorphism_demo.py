import math

# Define the base class Shape
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this!")

# Define the derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Define the derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Example usage (uncomment to test)
# if __name__ == "__main__":
#     shapes = [Rectangle(10, 5), Circle(7)]
#     for shape in shapes:
#         print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

from polymorphism_demo import Rectangle, Circle

def main():
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(10, 5)
    circle = Circle(7)

    # List of shapes
    shapes = [rectangle, circle]

    # Calculate and print the area of each shape
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
