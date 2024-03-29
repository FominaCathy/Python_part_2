"""
📌 Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений(отрицательных).
📌 Используйте декораторы свойств.
"""

'''
Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

'''


class ValidSize:
    def __init__(self, name):
        self.name = name

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.param_name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f'error size {self.name}: size <= 0')
        instance.__dict__[self.param_name] = value


class Rectangle:
    height = ValidSize('_height')
    width = ValidSize('_width')

    def __init__(self, height, width=None):

        self.height = height
        if width:
            self.width = width
        else:
            self.width = height

    @property
    def perimetr(self):
        return 2 * (self.height + self.width)

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f'прямоугольник ({self.height} x {self.width})'


if __name__ == "__main__":
    rect = Rectangle(2, -5)

    # print(rect.area)
    rect.width = 10
    print(rect)
    print(rect.area)
    rect.width = 20
    print(rect)
