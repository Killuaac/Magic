import math


class RightTriangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = math.sqrt(a ** 2 + b ** 2)

    def increase_side(self, percent):
        self.a *= (1 + percent / 100)
        self.b *= (1 + percent / 100)
        self.c = math.sqrt(self.a ** 2 + self.b ** 2)

    def decrease_side(self, percent):
        self.a *= (1 - percent / 100)
        self.b *= (1 - percent / 100)
        self.c = math.sqrt(self.a ** 2 + self.b ** 2)

    def calculate_circumradius(self):
        return self.c / 2

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_angles(self):
        alpha = math.degrees(math.asin(self.a / self.c))

        beta = math.degrees(math.asin(self.b / self.c))
        gamma = 90
        return alpha, beta, gamma


triangle = RightTriangle(3, 4)
print("Исходный треугольник:")
print(f"Сторона a: {triangle.a}")
print(f"Сторона b: {triangle.b}")
print(f"Сторона c (гипотенуза): {triangle.c}")
print(
    f"\nРадиус описанной окружности: {round(triangle.calculate_circumradius(), 2)}")
print(f"Периметр треугольника: {round(triangle.calculate_perimeter(), 2)}")

angles = triangle.calculate_angles()
print(f"\nУгол α: {round(angles[0], 2)} градусов")
print(f"Угол β: {round(angles[1], 2)} градусов")
print(f"Угол γ: {round(angles[2], 2)} градусов")
triangle.increase_side(10)  # Увеличиваем стороны на 10%
print("\nТреугольник после увеличения:")
print(f"Сторона a: {round(triangle.a, 2)}")
print(f"Сторона b: {round(triangle.b, 2)}")
print(f"Сторона c (гипотенуза): {round(triangle.c, 2)}")

triangle.decrease_side(10)  # Уменьшение стороны на 10%
print("\nТреугольник после уменьшения:")
print(f"Сторона a: {round(triangle.a, 2)}")
print(f"Сторона b: {round(triangle.b, 2)}")
print(f"Сторона c (гипотенуза): {round(triangle.c, 2)}")
