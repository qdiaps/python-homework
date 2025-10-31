from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

circle = Circle(radius=10)
rectangle = Rectangle(width=8, height=5)
triangle = Triangle(base=10, height=4)

print(f"Площа кола (радіус 10): {circle.calculate_area():.2f}")
print(f"Площа прямокутника (8x5): {rectangle.calculate_area()}")
print(f"Площа трикутника (основа 10, висота 4): {triangle.calculate_area()}")
