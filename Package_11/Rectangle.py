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
'''
1.Добавьте сравнение прямоугольников по площади: Должны работать все шесть операций сравнения
2.Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
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

    def __str__(self):
        return f'прямоугольник ({self.width}х{self.height}), S= {self.get_area()}'

    def __repr__(self):
        return f'размеры:({self.width}х{self.height}), S= {self.get_area()}'

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

    def __eq__(self, other):
        """равно"""
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        """не равно"""
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        """больше"""
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        """больше или равно"""
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        """меньше"""
        return self.get_area() < other.get_area()

    def __le__(self, other):
        """меньше или равно"""
        return self.get_area() <= other.get_area()


spam = Rectangle(10)
eggs = Rectangle(4, 3)
kuk = Rectangle(2, 6)

add_reg = spam + eggs
sub_reg = spam - eggs

# print(f'{sub_reg.width = }, {sub_reg.height =}')
# print(f'{add_reg.width = }, {add_reg.height =}')
# print(f'{spam.get_area() =}')
# print(f'{spam.get_perimetr()= }')
# print(f'{eggs.get_area()= }')
# print(f'{eggs.get_perimetr()= }')


print('\nСравнение (равно)')
print(f'{eggs}, {kuk}, равны: {eggs == kuk}')
print(f'{spam}, {kuk}, равны: {spam == kuk}')

print('\nСравнение (НЕ равно)')
print(f'{eggs}, {kuk}, НЕ равны: {eggs != kuk}')
print(f'{spam}, {kuk} НЕ равны: {spam != kuk}')

print('\nСравнение (меньше или равно)')
print(f'{eggs}, {kuk}, меньше или равно: {eggs <= kuk}')
print(f'{spam}, {kuk}, меньше или равно: {spam <= kuk}')
print(f'{kuk}, {spam}, меньше или равно: {kuk <= spam}')

print('\nСравнение (больше или равно)')
print(f'{eggs}, {kuk}, больше или равно: {eggs >= kuk}')
print(f'{spam}, {kuk}, больше или равно: {spam >= kuk}')
print(f'{kuk}, {spam}, больше или равно: {kuk >= spam}')

print('\nСравнение (меньше)')
print(f'{eggs}, {kuk}, меньше: {eggs < kuk}')
print(f'{spam}, {kuk}, меньше: {spam < kuk}')
print(f'{kuk}, {spam}, меньше: {kuk < spam}')

print('\nСравнение (больше)')
print(f'{eggs= }, {kuk= }, больше: {eggs > kuk}')
print(f'{spam= }, {kuk= }, больше: {spam > kuk}')
print(f'{kuk= }, {spam= }, больше: {kuk > spam}')
