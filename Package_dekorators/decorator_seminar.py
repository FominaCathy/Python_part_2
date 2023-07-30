"""
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""
from typing import Callable
from random import randint

__all__ = ['fun_secret']


def fun_top(num: int, count: int) -> Callable[[], None]:
    def fun_down():
        current_num = randint(1, num)
        for item in range(1, count + 1):
            spam = int(input(f'введите число в дианазоне от 1 до {num} (попытка № {item}): \n'))
            if spam == current_num:
                print('верно')
                break
            elif spam > current_num:
                print('меньше')
            else:
                print('больше')

    return fun_down


"""
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор. Он должен проверять входят ли переданные 
в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.
"""


def fun_decor(fun: Callable) -> Callable[[int, int], None]:
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


@fun_decor
def fun_secret(num: int, count: int):
    current_num = randint(1, num)
    for item in range(1, count + 1):
        spam = int(input(f'введите число в дианазоне от 1 до {num} (попытка № {item} из {count}): \n'))
        if spam == current_num:
            print('верно')
            break
        elif spam > current_num:
            print('меньше')
        else:
            print('больше')


if __name__ == '__main__':
    fun_secret(50, 8)
