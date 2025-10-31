class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print(f"Створено прямокутник з розмірами {self.width}x{self.height}")

    def calculate_area(self):
        return self.width * self.height

rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 12)

area1 = rect1.calculate_area()
print(f"Площа прямокутника 1 ({rect1.width}x{rect1.height}): {area1}")

print(f"Площа прямокутника 2 ({rect2.width}x{rect2.height}): {area2}")
