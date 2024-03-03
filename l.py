from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    def set_width(self, width):
        pass

    def set_height(self, height):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return math.pi * self.radius ** 2

    def set_width(self, width):
        self.radius = width / 2

    def set_height(self, height):
        self.radius = height / 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def get_area(self):
        return 0.5 * self.base * self.height

def main():
    circle = Circle(5)
    rectangle = Rectangle(3, 4)
    triangle = Triangle(3, 4)

    # Using common interface methods
    circle.set_width(10)
    print("Circle's area after setting width:", circle.get_area())

    rectangle.set_height(5)
    print("Rectangle's area after setting height:", rectangle.get_area())

    print("Triangle's area:", triangle.get_area())

if __name__ == "__main__":
    main()