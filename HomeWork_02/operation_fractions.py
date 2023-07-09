'''
3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение дробей.
Для проверки своего кода используйте модуль fractions.
'''

from fractions import Fraction


def input_fraction(promt: str) -> tuple:
    flag: bool = False

    while not flag:
        current_input = input(promt)
        flag = check_is_fraction(current_input)

    temp = current_input.split('/')
    return int(temp[0]), int(temp[1])


def check_is_fraction(current_str: str) -> bool:
    temp = current_str.split('/')

    if len(temp) != 2:
        return False
    elif temp[1].isdigit():
        if int(temp[1]) == 0:
            print('ВНИМАНИЕ!: делитель не может быть равен нулю')
            return False
        elif temp[0].isdigit() or len(temp[0]) > 1 and temp[0][1:].isdigit() and temp[0][0] == '-':  # отриц число
            return True

    return False


def simple_fraction(num, denom: int) -> str:
    for item in range(int(min(abs(num) ** 0.5, denom ** 0.5) + 1) + 1, 1, -1):
        if num % item == 0 and denom % item == 0:
            num /= item
            denom /= item
    return f'{int(num)}/{int(denom)}'


def multiple_fraction(f_first, f_second: tuple) -> str:
    return simple_fraction(f_first[0] * f_second[0], f_first[1] * f_second[1])


def summ_fractions(f_first, f_second: tuple) -> str:
    numerator: int
    denominator: int
    if f_first[1] == f_second[1]:
        numerator = f_first[0] + f_second[0]
        denominator = f_first[1]
    else:
        numerator = f_first[0] * f_second[1] + f_second[0] * f_first[1]
        denominator = f_first[1] * f_second[1]

    return simple_fraction(numerator, denominator)


fraction_first = input_fraction('введите первую дробь: в формате a/b:\n')
fraction_second = input_fraction('введите вторую дробь: в формате a/b:\n')

f1 = Fraction(fraction_first[0], fraction_first[1])
f2 = Fraction(fraction_second[0], fraction_second[1])

print(f'сумма дробей = {summ_fractions(fraction_first, fraction_second)}')
print(f'проверочное значение = {f1 + f2}')

print(f'произведение дробей = {multiple_fraction(fraction_first, fraction_second)}')
print(f'проверочное значение = {f1 * f2}')
