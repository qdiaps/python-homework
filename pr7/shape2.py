from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

def print_figure_area(shape: Shape):
    print(f"Площа фігури ({shape.__class__.__name__}): {shape.area()}")

my_circle = Circle(10)
my_square = Square(7)

print_figure_area(my_circle)
print_figure_area(my_square)
