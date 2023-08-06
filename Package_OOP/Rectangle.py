"""
Создайте класс прямоугольник.
📌 Класс должен принимать длину и ширину при создании экземпляра.
📌 У класса должно быть два метода, возвращающие периметр и площадь.
📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
"""
'''
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр прямоугольника.
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений.
'''


class Rectangle:

    def __init__(self, height: int, width=None):
        self.height = height
        if width:
            self.width = width
        else:
            self.width = height

    def get_perimetr(self):
        return 2 * (self.height + self.width)

    def get_area(self):
        return self.width * self.height

    def __add__(self, other):

        perimetr = self.get_perimetr() + other.get_perimetr()
        side_a = perimetr // 6
        side_b = (perimetr - side_a * 2) // 2

        return Rectangle(side_a, side_b)

    def __sub__(self, other):

        perimetr = abs(self.get_perimetr() - other.get_perimetr())
        side_a = perimetr // 6
        side_b = (perimetr - side_a * 2) // 2

        return Rectangle(side_a, side_b)


spam = Rectangle(1, 9)
eggs = Rectangle(7)

add_reg = spam + eggs
sub_reg = spam - eggs

print(f'{sub_reg.width = }, {sub_reg.height =}')
print(f'{add_reg.width = }, {add_reg.height =}')
# print(f'{spam.get_area() =}')
# print(f'{spam.get_perimetr()= }')
# print(f'{eggs.get_area()= }')
# print(f'{eggs.get_perimetr()= }')
