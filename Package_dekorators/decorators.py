'''
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.+
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.+
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
'''
import csv
import json
from random import uniform
from typing import Callable

__all__ = ['generator_csv_file', 'get_quadratic_roots']

MIN_KOEFF = -200
MAX_KOEFF = 200


def generator_csv_file(count: int, file_csv: str):
    with open(file_csv, 'w', newline='') as fc:
        csv_write = csv.writer(fc, dialect='excel')
        for i in range(count):
            csv_write.writerow(
                [round(uniform(MIN_KOEFF, MAX_KOEFF), 2), round(uniform(MIN_KOEFF, MAX_KOEFF), 2),
                 round(uniform(MIN_KOEFF, MAX_KOEFF), 2)])


# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.

def decor_group_solved(fun: Callable) -> Callable[[str], None]:
    def wrapper(args):
        file_csv, *_ = args
        list_result = []
        with open(file_csv, 'r', newline='') as fc:
            csv_read = csv.reader(fc, dialect='excel')
            for line in csv_read:
                a, b, c = map(float, line)
                list_result.append({'a': a, 'b': b, 'c': c, 'res': fun(a, b, c)})

        return list_result

    return wrapper


# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
def decor_saved_result_json(fun: Callable):
    def wrapper(*args):
        res = fun(args)
        with open('result.json', 'w', encoding='utf-8') as fj:
            json.dump(res, fj, indent=2)

    return wrapper


@decor_saved_result_json
@decor_group_solved
def get_quadratic_roots(*args) -> list:
    a, b, c = map(float, args)

    d = b ** 2 - 4 * a * c
    if a == 0:
        x1 = x2 = (d - c) / b
        return [x1, x2]

    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = -(-b - d ** 0.5) / (2 * a)
        return [x1, x2]
    elif d == 0:
        x = -b / (2 * a)
        return [x]
    else:
        d = complex(d, 0)
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return [{'type': 'complex', 'real': x1.real, 'imag': x1.imag},
                {'type': 'complex', 'real': x2.real, 'imag': x2.imag}]


if __name__ == '__main__':
    # generator_csv_file(100, 'koeff.csv')
    get_quadratic_roots('koeff.csv')
