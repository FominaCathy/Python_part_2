'''
задача 7
Создайте модуль и напишиите в нем функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может сущестровать или ложь, если такая дата невозможна
год в диапазоне [1, 9999]
весь период действует Григорианский календарь
проверу года на високосность вынести в отдельную защищенную функцию
'''

from sys import argv

__all__ = ['check_exist_data']

SHORT_MONTH = {2, 4, 6, 9, 11}
LONG_MONTH = {1, 3, 5, 7, 8, 10, 12}

YEAR_REFORM = 1


def _check_leap_year(year):
    if year <= YEAR_REFORM:
        return True if year % 4 == 0 else False
    elif (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False


def check_exist_data(curr_data='01.01.1001') -> bool:
    """проверка существования даты

    :param curr_data: дата в формате DD.MM.YYYY
    :return: False or True
    """

    day, month, year = (int(i) for i in curr_data.split('.'))

    if month != 2:
        return (month in LONG_MONTH and 1 <= day <= 31) or (month in SHORT_MONTH and 1 <= day <= 30)
    elif month == 2:
        if _check_leap_year(year):
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28

    return False


def check_valid_input(check_data) -> bool:
    spam = check_data.split('.')
    if (len(spam) != 3) or not all((item.isdigit() for item in spam)):
        print('некорректный ввод. ввод не соответствует формату: DD.MM.YYYY')
        return False
    elif int(spam[2]) < 1 or int(spam[2]) > 9999:
        print('год не входит в диапазон проверки')
        return False

    return True


'''
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''
if __name__ == '__main__':
    if len(argv) == 2:
        curr_date = argv[1]
    else:
        curr_date = input('введите дату в формате DD.MM.YYYY: ')

    if check_valid_input(curr_date):
        print(f'{curr_date} - существует') if check_exist_data(curr_date) else print(f'{curr_date} - НЕ существует')
