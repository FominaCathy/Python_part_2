"""
Создайте класс окружность.
📌 Класс должен принимать радиус окружности при создании
экземпляра.
📌 У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_circuit(self):
        return math.pi * 2 * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2




n = Circle(7)
print(n.get_circuit())
print(n.get_area())


