'''
Создайте класс Архив, который хранит пару свойств. Например, число и строку.
При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов,
которые также являются свойствами экземпляра.
'''

'''
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста и для пользователя.
'''

class Arhiv:
    """класс Архив. хранит пару свойств: строку и число."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_arhiv = []

        cls._instance.list_arhiv.append([args])

        return cls._instance

    def __init__(self, text: str, number: int):
        self.text = text
        self.number = number

    def __str__(self):

        return f'текущий текст строки: {self.text}, число строки: {self.number}'

    def __repr__(self):
        return f'{self.text}, {self.number}'




spam = Arhiv("ночной страж", 65)
print(spam)
print(f'{spam.text}, {spam.number}')
spam3 = Arhiv("дневной дозор", 1555)
print(f'{spam.text =}, {spam.number =}')

print(f'{spam.list_arhiv}')

