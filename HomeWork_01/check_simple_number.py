'''3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки:
“Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.'''
import math

LOWER_LIMIT = 0
UPPER_LIMIT = 100000


def check_simple_number(number):
    if number > 3:
        for i in range(2, math.ceil(number ** 0.5) + 1):
            if number % i == 0:
                return False
    return True


num = None
while num not in range(LOWER_LIMIT, UPPER_LIMIT + 1):
    print('введите число от ', LOWER_LIMIT, 'до', UPPER_LIMIT, ': ')
    num = int(input())
else:
    print('число', num, 'простое' if check_simple_number(num) else 'составное')
