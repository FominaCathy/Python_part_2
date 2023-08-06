'''
Задание №5
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и +
○ декоратором для многократного запуска. +
Выберите верный порядок декораторов.

задание 6
Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.

'''

from typing import Callable
from random import randint
from functools import wraps

__all__ = ['game_guessing']
'''
декоратор контроля значений (Дорабатываем задачу 1.)
Превратите внешнюю функцию в декоратор. Он должен проверять входят ли переданные в функцию угадайку числа в 
диапазоны [1, 100] и [1, 10]. Если не входят, вызывать функцию со случайными числами из диапазонов.
'''
_list_cache = list()


def decor_control_count(fun: Callable) -> Callable[[int, int], None]:
    @wraps(fun)
    def wrapper(*args):
        num, count = args
        if num not in range(1, 101) and count not in range(1, 11):
            return fun(randint(1, 100), randint(1, 10))
        elif num in range(1, 101) and count not in range(1, 11):
            return fun(num, randint(1, 10))
        elif num not in range(1, 101) and count in range(1, 11):
            return fun(randint(1, 100), count)
        else:
            return fun(num, count)

    return wrapper


'''
декоратор для многократного запуска.
'''


def decor_repeat(count: int = 1):
    def fun_decor_session(fun: Callable) -> Callable[..., None]:
        @wraps(fun)
        def wrapper(*args):
            for i in range(count):
                print(f'сессия игры № {i + 1}')
                result = fun(*args)
            return result

        return wrapper

    return fun_decor_session


'''
декоратор для сохранения параметров, 
(буду сохранять список кортежей из аргументов и загаданного числа):
'''


def decor_cache(fun: Callable):
    @wraps(fun)
    def wrapper(*args):
        res = fun(*args)
        _list_cache.append((args, res))
        return res

    return wrapper


@decor_repeat(3)
@decor_control_count
@decor_cache
def game_guessing(num: int, count: int):
    current_num = randint(1, num)
    for item in range(1, count + 1):
        spam = int(input(f'введите число в дианазоне от 1 до {num} (попытка № {item} из {count}): \n'))
        if spam == current_num:
            print(f'верно! загаданное число {current_num}')
            break
        elif spam > current_num:
            print('меньше')
        else:
            print('больше')

    return current_num


if __name__ == '__main__':
    game_guessing(50, 3)
    print(_list_cache)
    print(help(game_guessing))
