'''
Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой функции.

'''

__all__ = ['print_hello', 'print_hello_group']

from typing import Callable
from random import randint

def fun_repeat(count: int = 1):
    def fun_decor_hello(fun: Callable) -> Callable[..., None]:
        def wrapper(*args):
            for i in range(count):
                print(f'попытка номер {i + 1}: ', end='')
                result = fun()
            return result

        return wrapper

    return fun_decor_hello


def fun_repeat_list(count: int = 1):
    def decor_hello_group(fun: Callable):
        def wrapper(args):
            spam = args
            for i in range(count):
                rnd = randint(0, len(spam))
                print(spam[rnd], end='')
                result = fun(args)
            return result

        return wrapper

    return decor_hello_group


@fun_repeat_list(3)
def print_hello_group(group: list):
    print(', hello, my friend')


@fun_repeat(5)
def print_hello():
    print("Hello, world!")


if __name__ == '__main__':
    print_hello() # повторяет 5раз привет
    list_friend = ['milka', 'kuku', 'troll', 'mu-mu', 'other']
    print_hello_group(list_friend) # здоровается с 3мя рандомными друзьями из списка
