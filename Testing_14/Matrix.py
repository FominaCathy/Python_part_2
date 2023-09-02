'''
3.Создайте класс Матрица. Добавьте методы для:
○ вывода на печать, +
○ сравнения,+
○ сложения,+
○ *умножения матриц
'''
import doctest
from copy import deepcopy
from random import randint, choices


class ExceptionMatrix(Exception):
    pass


class NotEqualSizeMatrix(ExceptionMatrix):
    def __init__(self, first_m, second_m, operation):
        self.first_m = first_m
        self.second_m = second_m
        self.operation = operation

    def __str__(self):
        return f'размеры матриц: {self.first_m} и {self.second_m} не совпадают. ' \
               f'операция "{self.operation}" не может быть выполнена'


class NotMultipleMatrix(ExceptionMatrix):
    def __init__(self, first_m, second_m):
        self.first_m = first_m
        self.second_m = second_m

    def __str__(self):
        return f'матрицы с размерами: {self.first_m} и {self.second_m} не могут быть перемножены'


class Matrix:

    def __init__(self, row: int, column=None):
        self.row = row
        self.column = column if column else row
        self.matrix = []
        for item in range(row):
            self.matrix.append([])

    def fill_row(self, number_row: int, list_row: list):
        """заполнение строки."""
        stopper = self.column - len(self.matrix[number_row - 1])
        self.matrix[number_row - 1].extend(list_row[:stopper])

    def get_random(self, min_value=0, max_value=10):
        """заполнение матрицы рандомными значениями"""
        for i in range(self.row):
            self.fill_row(i, choices(range(min_value, max_value + 1), k=self.column))

    # TODO сделать размер сепаратора динамически определяемым в зависимости от длины числа
    def __str__(self):
        """формирует строку для печати матрицы"""
        spam = [item for row in self.matrix for item in row]
        sep_elem: int = len(str(max(spam))) + 2
        for_print = ""
        for i, elem in enumerate(spam, start=1):
            for_print += f'{elem:{sep_elem}}'
            if i % self.column == 0:
                for_print += '\n'
        return for_print

    @property
    def size(self):
        return f'({self.row}x{self.column})'

    # TODO заменить i на "enumerate" (не получилось)
    def __add__(self, other):
        """
        >>> (matrix3x2_one + matrix3x2_other) == summ_matrix
        True
        >>> (matrix3x2_one + matrix3x2_one) == summ_matrix
        False
        >>> (matrix3x2_other + other_matrix)
        размеры матриц: (3x2) и (2x3) не совпадают. операция "сложение" не может быть выполнена
        """
        try:
            if self.row != other.row or self.column != other.column:
                raise NotEqualSizeMatrix(self.size, other.size, 'сложение')
            summ_matrix = Matrix(self.row, self.column)
            i = 1
            for left, right in zip(self.matrix, other.matrix):
                summ_matrix.fill_row(i, [(le + ri) for le, ri in zip(left, right)])
                i += 1
            return summ_matrix
        except ExceptionMatrix as em:
            print(em)

    def __mul__(self, other):
        try:
            if (self.row == other.column) and (self.column == other.row):
                left = self.matrix
                right = other.matrix
                mult_matrix = Matrix(self.row, other.column)

                for row in range(self.row):
                    mult_row = []
                    for col in range(other.column):
                        item = sum(x * y for x, y in zip(left[row], [right[i][col] for i in range(other.row)]))
                        mult_row.append(item)

                    mult_matrix.fill_row(row - 1, mult_row)
                return mult_matrix
            else:
                raise NotMultipleMatrix(self.size, other.size)
        except ExceptionMatrix as em:
            print(em)
            return None

    def __eq__(self, other):
        """равно: Две матрицы называются равными, если они одинакового размера и соотв. элементы обеих матриц равны.
        >>> matrix3x2_double == matrix3x2_one
        True
        >>> matrix3x2_double == matrix3x2_other
        False
        >>> matrix3x2_double == other_matrix
        размеры матриц: (3x2) и (2x3) не совпадают. операция "сравнение" не может быть выполнена
        """

        try:
            if self.row != other.row or self.column != other.column:
                raise NotEqualSizeMatrix(self.size, other.size, 'сравнение')
            matrix_left = [item for row in self.matrix for item in row]
            matrix_right = [item for row in other.matrix for item in row]

            return all(left == right for left, right in zip(matrix_left, matrix_right))

        except ExceptionMatrix as em:
            print(em)

    def __ne__(self, other):
        """не равно
        >>> matrix3x2_double != matrix3x2_one
        False
        >>> matrix3x2_double != matrix3x2_other
        True
        >>> matrix3x2_double != other_matrix
        True

        """
        if (self.row != other.row) or (self.column != other.column):
            return True
        else:
            matrix_left = [item for row in self.matrix for item in row]
            matrix_right = [item for row in other.matrix for item in row]

            return any(left != right for left, right in zip(matrix_left, matrix_right))

    def determinant(self):

        def det(curr_matrix: list) -> int:
            cur_det = 0
            if len(curr_matrix) == len(curr_matrix[0]) and len(curr_matrix[0]) == 1:
                return curr_matrix[0][0]
            else:
                sub_list = curr_matrix[0]
                for i, item in enumerate(sub_list, start=0):
                    spam = deepcopy(curr_matrix)
                    spam.pop(0)
                    for j in range(len(spam)):
                        spam[j].pop(i)
                        cur_det += item * (-1) ** (2 + i) * det(spam)
                return cur_det

        return det(self.matrix)

    def __gt__(self, other):
        """больше. т.к. понятия "больше" и "меньше" неприменимы к матрицам - будем сравнивать детерминант"""
        return self.determinant() > other.determinant()

    def __ge__(self, other):
        """больше или равно"""
        return (self.determinant() > other.determinant()) or (self == other)

    def __lt__(self, other):
        """меньше т.к. понятия "больше" и "меньше" неприменимы к матрицам - будем сравнивать детерминант"""
        return self.determinant() < other.determinant()

    def __le__(self, other):
        """меньше или равно"""
        return (self.determinant() < other.determinant()) or (self == other)


if __name__ == "__main__":
    matrix_random = Matrix(5, 7)
    matrix_random.get_random(0, 10)

    matrix3x2_one = Matrix(3, 2)
    matrix3x2_one.fill_row(1, [3, 5, 10, 45])
    matrix3x2_one.fill_row(2, [1, 2, 3, 4, 5, 6, 7])
    matrix3x2_one.fill_row(3, [4, 5, 6, 7])

    matrix3x2_double = Matrix(3, 2)
    matrix3x2_double.fill_row(1, [3, 5])
    matrix3x2_double.fill_row(2, [1, 2])
    matrix3x2_double.fill_row(3, [4, 5])

    matrix3x2_other = Matrix(3, 2)
    matrix3x2_other.fill_row(1, [3, 4])
    matrix3x2_other.fill_row(2, [1, 6])
    matrix3x2_other.fill_row(3, [0, 5])

    other_matrix = Matrix(2, 3)
    other_matrix.fill_row(1, [2, 5, 69, 46])
    other_matrix.fill_row(2, [1, 2, 3, 4, 5, 6, 7])

    summ_matrix = Matrix(3, 2)
    summ_matrix.fill_row(1, [6, 9])
    summ_matrix.fill_row(2, [2, 8])
    summ_matrix.fill_row(3, [4, 10])

    # print(matrix_one != other_matrix)

    # print(f'{other_matrix.determinant() = }')
    # print(f'{matrix_one.determinant() = }')
    # d_other = other_matrix.determinant()
    # d_one = matrix_one.determinant()

    # print(matrix3x2_one+ matrix3x2_other)

    # print(f'other_matrix (D={d_other}) > matrix_one (D={d_one}) -{other_matrix > matrix_one}')
    # print(f'other_matrix (D={d_other}) >= matrix_one (D={d_one}) -{other_matrix >= matrix_one}')
    # print(f'other_matrix (D={d_other}) < matrix_one (D={d_one}) -{other_matrix < matrix_one}')
    # print(f'other_matrix (D={d_other}) <= matrix_one (D={d_one}) -{other_matrix <= matrix_one}')

    doctest.testmod(verbose=True)
