'''
3.Создайте класс Матрица. Добавьте методы для:
○ вывода на печать, +
○ сравнения,+
○ сложения,+
○ *умножения матриц
'''
from copy import deepcopy
from random import randint, choices


class Matrix:

    def __init__(self, row: int, column=None):
        self.row = row
        self.column = column if column else row
        self.matrix = []
        for item in range(row):
            self.matrix.append([])
        # print(self.matrix)

    def fill_row(self, number_row: int, list_row: list):
        """заполнение строки."""
        stopper = self.column - len(self.matrix[number_row - 1])
        self.matrix[number_row - 1].extend(list_row[:stopper])
        # print(self.matrix)

    def get_random(self, min_value=0, max_value=10):
        """заполнение матрицы рандомными значениями"""
        for i in range(self.row):
            self.fill_row(i, choices(range(min_value, max_value + 1), k=self.column))
        # print(self.matrix)

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

    # TODO заменить i на "enumerate" (не получилось)
    def __add__(self, other):
        summ_matrix = Matrix(self.row, self.column)
        i = 1
        for left, right in zip(self.matrix, other.matrix):
            summ_matrix.fill_row(i, [(le + ri) for le, ri in zip(left, right)])
            i += 1
        return summ_matrix

    def __mul__(self, other):

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
            return None

    def __eq__(self, other):
        """равно: Две матрицы называются равными, если они одинакового размера и соотв. элементы обеих матриц равны."""
        if (self.row == other.row) and (self.column == other.column):
            matrix_left = [item for row in self.matrix for item in row]
            matrix_right = [item for row in other.matrix for item in row]

            return all(left == right for left, right in zip(matrix_left, matrix_right))

        else:
            return False

    def __ne__(self, other):
        """не равно"""
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
        return (self.determinant() > other.determinant()) or (self.determinant() == other.determinant())

    def __lt__(self, other):
        """меньше т.к. понятия "больше" и "меньше" неприменимы к матрицам - будем сравнивать детерминант"""
        return self.determinant() < other.determinant()

    def __le__(self, other):
        """меньше или равно"""
        return (self.determinant() < other.determinant()) or (self.determinant() == other.determinant())


if __name__ == "__main__":
    matrix = Matrix(5, 7)
    matrix.get_random(0, 10)
    # print(matrix)

    matrix_one = Matrix(3, 2)
    matrix_one.fill_row(1, [3, 5, 10, 45])
    matrix_one.fill_row(2, [1, 2, 3, 4, 5, 6, 7])
    matrix_one.fill_row(3, [4, 5, 6, 7])
    print(matrix_one)

    other_matrix = Matrix(2, 3)
    other_matrix.fill_row(1, [2, 5, 69, 46])
    other_matrix.fill_row(2, [1, 2, 3, 4, 5, 6, 7])
    print(other_matrix)

    # print(matrix_one != other_matrix)
    # print(matrix != other_matrix)

    # print(other_matrix + matrix_one)

    # print(f'{other_matrix.determinant() = }')
    # print(f'{matrix_one.determinant() = }')
    # d_other = other_matrix.determinant()
    # d_one = matrix_one.determinant()
    #
    # print(f'other_matrix (D={d_other}) > matrix_one (D={d_one}) -{other_matrix > matrix_one}')
    # print(f'other_matrix (D={d_other}) >= matrix_one (D={d_one}) -{other_matrix >= matrix_one}')
    # print(f'other_matrix (D={d_other}) < matrix_one (D={d_one}) -{other_matrix < matrix_one}')
    # print(f'other_matrix (D={d_other}) <= matrix_one (D={d_one}) -{other_matrix <= matrix_one}')

    print(matrix_one * other_matrix)
