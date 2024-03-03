from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def get_area(self):
        print("hi")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        import math
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == "Circle":
            return Circle(*args)
        elif shape_type == "Square":
            return Square(*args)
        elif shape_type == "Rectangle":
            return Rectangle(*args)
        else:
            raise ValueError("Unsupported shape type")

def main():
    obj = ShapeFactory()
    temp = obj.create_shape("Square", 5)
    print("Area of Square:", temp.get_area())

if __name__=="__main__":
    main()