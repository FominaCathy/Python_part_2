import unittest
from Matrix import Matrix, NotEqualSizeMatrix
from unittest.mock import patch
import io


class BaseForTest:
    @property
    def matrix3x2_one(self):
        matrix3x2_one = Matrix(3, 2)
        matrix3x2_one.fill_row(1, [3, 5, 10, 45])
        matrix3x2_one.fill_row(2, [1, 2, 3, 4, 5, 6, 7])
        matrix3x2_one.fill_row(3, [4, 5, 6, 7])
        return matrix3x2_one

    @property
    def matrix3x2_double(self):
        matrix3x2_double = Matrix(3, 2)
        matrix3x2_double.fill_row(1, [3, 5])
        matrix3x2_double.fill_row(2, [1, 2])
        matrix3x2_double.fill_row(3, [4, 5])
        return matrix3x2_double

    @property
    def matrix3x2_other(self):
        matrix3x2_other = Matrix(3, 2)
        matrix3x2_other.fill_row(1, [3, 4])
        matrix3x2_other.fill_row(2, [1, 6])
        matrix3x2_other.fill_row(3, [0, 5])
        return matrix3x2_other

    @property
    def summ_matrix3x2(self):  # matrix3x2_one + matrix3x2_other
        summ_matrix3x2 = Matrix(3, 2)
        summ_matrix3x2.fill_row(1, [6, 9])
        summ_matrix3x2.fill_row(2, [2, 8])
        summ_matrix3x2.fill_row(3, [4, 10])
        return summ_matrix3x2

    @property
    def other_matrix(self):
        other_matrix = Matrix(2, 3)
        other_matrix.fill_row(1, [2, 5, 69, 46])
        other_matrix.fill_row(2, [1, 2, 3, 4, 5, 6, 7])
        return other_matrix


class TestCase(unittest.TestCase):
    matrix3x2_one = BaseForTest.matrix3x2_one
    matrix3x2_double = BaseForTest.matrix3x2_double
    matrix3x2_other = BaseForTest.matrix3x2_other
    summ_matrix3x2 = BaseForTest.summ_matrix3x2
    other_matrix = BaseForTest.other_matrix

    def test_equal_valid(self):
        self.assertTrue(self.matrix3x2_one == self.matrix3x2_double)

    def test_equal_non_valid(self):
        self.assertFalse(self.matrix3x2_one == self.matrix3x2_other)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_non_equal_different_size_valid(self, mock_stdout):
        eggs = self.matrix3x2_one == self.other_matrix
        self.assertEqual(mock_stdout.getvalue(),
                         'размеры матриц: (3x2) и (2x3) не совпадают. операция "сравнение" не может быть выполнена\n')

    def test_summ_valid(self):
        eggs = (self.matrix3x2_one + self.matrix3x2_other)
        self.assertTrue(eggs, self.summ_matrix3x2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
