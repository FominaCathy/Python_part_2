'''
Создайте класс проекта, который имеет следующие методы:
загрузка данных (функция из задания 4)

вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из множества пользователей.

добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.

Задание №6
Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
Передавайте необходимые данные из основного кода проекта.
'''
import argparse
from datetime import datetime
import json
import logging
from pathlib import Path


class ValidLevel:
    def __init__(self, level):
        self.level = level

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.param_name]

    def __set__(self, instance, value):
        # оставила чтобы падал.
        if value > instance._MAX_LEVEL or value < instance._MIN_LEVEL:
            raise ValueError(
                f"уровень доступа должен быть в диапазоне от {instance._MIN_LEVEL} до {instance._MAX_LEVEL}")

        instance.__dict__[self.param_name] = value


class Person:
    _MIN_LEVEL = 1
    _MAX_LEVEL = 8
    level = ValidLevel('_level')

    def __init__(self, name, num_id, level):
        self.level = level
        self.name = name
        self.num_id = num_id

    def __str__(self):
        return f'name: {self.name}, id: {self.num_id}, level: {self.level}'

    def __eq__(self, other):
        return self.num_id == other.num_id and self.name == other.name

    def __hash__(self):
        return hash((self.num_id, self.name))


class ExceptionProject(Exception):
    pass


class AccessError(ExceptionProject):
    def __init__(self, user: Person):
        self.user = user

    def __str__(self):
        return f'пользователь "{self.user.name}, id: {self.user.num_id}" не может зайти в проект: нет списке группы проекта'


class LevelError(ExceptionProject):
    def __init__(self, user: Person, actor: str):
        self.actor = actor
        self.user = user

    def __str__(self):
        return f"пользователь {self.user.name} не может {self.actor}: низкий уровень доступа ({self.user.level})"


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
            logger.error(f'ошибка проекта: {exp}, время запуска {datetime.now()}')
            print(f'файл с данными пользователей не найден: {exp}')

    def authorize(self, name, num_id):

        try:
            user = Person(name, num_id, 1)
            for item in self.team:
                if user == item:
                    user.level = item.level
                    if user.level < self.level_owner:
                        raise LevelError(user, 'зайти в проект')
                    else:
                        print(f'{user.name}, Добро пожаловать в проект')
                        return
            raise AccessError(user)

        except ExceptionProject as exp:
            logger.error(f'ошибка проекта: {exp}, время запуска {datetime.now()}')
            print(exp)

    def add_user(self, user: Person):
        try:
            if user.level < self.level_owner:
                raise LevelError(user, 'добавлен в проект')
            self.team.add(user)
            print('пользоваатель добавлен в проект')
        except LevelError as exp:
            logger.error(f'ошибка проекта: {exp}, время запуска {datetime.now()}')
            print(exp)


if __name__ == "__main__":

    logging.basicConfig(filename='logger_project.log', style='{', filemode='a', encoding='utf-8', level=logging.NOTSET)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='project')
    parser.add_argument('-lo', metavar='lo', type=int, default=0, help='уровень владельца проекта')
    parser.add_argument('-name', metavar='name', type=str, default=None, help='имя пользователя')
    parser.add_argument('-id', metavar='id', type=str, default=None, help='id пользователя')
    parser.add_argument('-l', metavar='l', type=int, default=None, help='уровень пользователя')
    parser.add_argument('-a', metavar='a', type=str, default=None, help='действие: add - добавление пользователя entr - вход')

    args = parser.parse_args()

    try:
        test_project = Project(args.lo)
        test_project.load_data('test_bd.json')
        logger.info(f'создан проект с уровнем пользователя: {args.lo}, время создания: {datetime.now()}')

        if args.a == 'add':
            worker = Person(args.name, args.id, args.l)
            logger.info(f'создан пользователь: {worker}, время создания: {datetime.now()}')
            test_project.add_user(worker)
            logger.info(f'пользователь: {worker} добавлен в проект, время добавления: {datetime.now()}')
        elif args.a == 'entr':
            test_project.authorize(args.name, args.id)
            logger.info(f'пользователь: {args.name} зашел в проект, время авторизации: {datetime.now()}')

    except Exception as exc:
        logger.critical(f'ошибка командной строки: {exc}, время запуска {datetime.now()}')
        print(f'ошибка: {exc}')

    # test_project = Project(4)
    # test_project.load_data('test_bd.json')

    # worker = Person('troll', '33e', 3)

    # print(worker)
    # test_project.authorize(worker.name, worker.num_id)
    # test_project.add_user(worker)
    # print('-' * 50)
    # test_project.authorize("ivan", "8p")
    # print('-' * 50)
    # test_project.authorize("macyanya", "lala")
    # print('-' * 50)
    # test_project.authorize("willy", "9e")
