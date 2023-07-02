'''
Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print
'''

YEAR_REFORM = 1582


def check_leap_year(year):
    if year <= YEAR_REFORM:
        return True if year % 4 == 0 else False
    elif (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False


year_check = int(input('введите год: '))

print(year_check, 'високосный год' if check_leap_year(year_check) else 'НЕ високосный год', sep=' - ')
