from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Повернути площу фігури"""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class AreaCalculator:
    def calculate_total_area(self, shapes):
        """
        Цей метод приймає список об'єктів, які наслідують Shape.
        Йому неважливо, чи це Circle, чи Rectangle.
        """
        total_area = 0
        for shape in shapes:
            total_area += shape.area()
        return total_area

shapes = [
    Circle(5),
    Rectangle(10, 4)
]

calculator = AreaCalculator()
print(f"Загальна площа (до): {calculator.calculate_total_area(shapes)}")

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes.append(Triangle(10, 5))

print(f"Загальна площа (після): {calculator.calculate_total_area(shapes)}")
