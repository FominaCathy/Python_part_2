# Напишите функцию для транспонирования матрицы
from random import randint

MIN_VALUE = 0
MAX_VALUE = 150
sh_print = len(str(MAX_VALUE)) + 2


def fill_matrix(coll: int, row: int):
    new_matrix = list(list())
    for i in range(0, row):
        current_row = []
        for j in range(0, coll):
            current_row.append(randint(MIN_VALUE, MAX_VALUE))
        new_matrix.append(current_row)
    return new_matrix


def fill_matrix_iter(coll: int, row: int):
    new_matrix: list(list()) = [[randint(MIN_VALUE, MAX_VALUE) for i in range(0, coll)] for j in range(0, row)]
    return new_matrix


def transposition_matrix(matrix: list(list())):
    count_row = len(matrix)
    count_coll = len(matrix[0])
    new_matrix = [[matrix[i][j] for i in range(0, count_row)] for j in range(0, count_coll)]
    return new_matrix


def print_matrix(matrix: list(list())):
    spam_row = iter(matrix)
    for i in range(0, len(matrix)):
        for item in next(spam_row):
            print(f'{item:> {sh_print}}', end='')
        print()


size_matrix = input(f'введите размеры матрицы (колонок и строк) через пробел: \n').split(' ')

spam = fill_matrix(int(size_matrix[0]), int(size_matrix[1]))
print(f'\n Исходная матрица: ')
print_matrix(spam)

print(f'\n Транспонированная матрица: ')

eggs = transposition_matrix(spam)
print_matrix(eggs)
