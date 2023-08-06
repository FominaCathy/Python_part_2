"""
Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
📌 У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
📌 Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст."""


class Human:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

if __name__ == '__main__':

    person = Human('Smit', 'Jon', 33)
    print(f'{person.get_full_name()=}')
    print(f'{person.get_age()=}')
    person.birthday()
    print(f'{person.get_age()=}')
