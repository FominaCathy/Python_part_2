'''
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print

'''

LOWER_LIMIT = 1
UPPER_LIMIT = 999


def reverse_number(num):
    new_number = 0
    digit = 100
    while num > 0:
        new_number += (num % 10) * digit
        digit /= 10
        num //= 10
    return f'введено 3х значное число. Результат: {int(new_number)}'


def get_result(number):
    if number in range(1, 10):
        return f'введена цифра. Результат: {number ** 2}'
    elif number in range(11, 100):
        return f'введено 2х значное число. Результат: {(number // 10) * (number % 10)}'
    else:
        return reverse_number(number)


current_num = None

while current_num not in range(LOWER_LIMIT, UPPER_LIMIT + 1):
    print('введите число от ', LOWER_LIMIT, 'до', UPPER_LIMIT, ': ')
    current_num = int(input())
else:
    print(get_result(current_num))
