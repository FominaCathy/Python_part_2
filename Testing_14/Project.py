'''
Создайте класс проекта, который имеет следующие методы:
загрузка данных (функция из задания 4)

вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из множества пользователей.

добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
Передавайте необходимые данные из основного кода проекта.


'''

import json
from pathlib import Path
import doctest
from Person import Person
import ExProject


class Project:

    def __init__(self, level_owner):
        self.level_owner = level_owner
        self.team = set()

    def load_data(self, file: Path):

        try:
            with open(file, 'r', encoding='utf-8') as fj:
                dict_bd = json.load(fj)

            for level, subdict in dict_bd.items():
                for id_cod, name in subdict.items():
                    self.team.add(Person(name, id_cod, int(level)))

        except FileNotFoundError as exp:
            print(f'файл с данными пользователей не найден: {exp}')

    def authorize(self, name, num_id):
        try:
            user = Person(name, num_id, 1)
            for item in self.team:
                if user == item:
                    user.level = item.level
                    if user.level < self.level_owner:
                        raise ExProject.LevelError(user, 'зайти в проект')
                    else:
                        print(f'{user.name}, Добро пожаловать в проект')
                        return
            raise ExProject.AccessError(user)

        except ExProject.ExceptionProject as exp:
            print(exp)

    def add_user(self, user: Person):

        try:
            if user.level < self.level_owner:
                raise ExProject.LevelError(user, 'добавлен в проект')
            self.team.add(user)
            print(f'пользователь {user} добавлен в проект')
        except ExProject.LevelError as exp:
            print(exp)


if __name__ == "__main__":
    doctest.testmod(verbose=True)
