import sys


def work1():
    a = 4
    print(type(a))
    a = 'esw'
    print(type(a))
    a = 2.1
    print(type(a))


# Создайте в переменной data список значений разных
# типов перечислив их через запятую внутри квадратных скобок.
# Для каждого элемента в цикле выведите:
#     порядковый номер начиная с единицы
#     значение
#     адрес в памяти
#     размер в памяти
#     хэш объекта
#     результат проверки на целое число только если он положительный
#     результат проверки на строку только если он положительный
#
# *Добавьте в список повторяющиеся элементы и сравните на результаты.


def work2():
    my_list = [21, 456, 'hello', True, 3, 'hello']
    for i, item in enumerate(my_list, 1):
        number_output = 'Это целое число' if isinstance(item, int) else ''
        str_output = 'Это строка' if isinstance(item, str) else ''
        print(f'номер: {i}; '
              f'значение: {item}; '
              f'Хэш объекта - {hash(item)};'
              f'{number_output}'
              f'{str_output}')


# Напишите программу, которая получает целое число
# и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.

# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
BINARY_SYSTEM = 2
OCTAL_SYSTEM = 8


def system_selection() -> int:
    system: int = 0

    while system != BINARY_SYSTEM and system != OCTAL_SYSTEM:
        system = int(input('\nВыберите систему счисления\n'
                           '2 - двоичная\n'
                           '8 - восьмиричная\n'))
        return system


def transfer_system(number: int, system: int) -> str:
    result: str = ''

    while number != 0:
        mod: str = str(number % system)
        result = mod + result
        number //= system

    return result


def work3():
    number: int = int(input('введите число:\n'))

    selection: int = system_selection()
    transfer: str = transfer_system(number, selection)

    print(f'\nРезультат: {transfer}')
    print(f'двоичная система: {bin(number)[2:]}')
    print(f'восьмеричная система: {oct(number)[2:]}')


# Напишите программу, которая вычисляет площадь круга и
# длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять
# не менее 42 знаков после запятой.

from decimal import Decimal, getcontext
from math import pi

getcontext().prec = 42
num_pi = Decimal(pi)

diametr: Decimal = 0
while diametr not in range(1, 1001):
    diametr = Decimal(input('введите диаметр от 1 до 1000:\n'))

area: Decimal = (num_pi * diametr ** 2 / 4)
length: Decimal = (num_pi * diametr)

print(f'площадь =  {area}')
print(f'длина: {length}')
