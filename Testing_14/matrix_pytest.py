import pytest
from Matrix import Matrix

@pytest.fixture
def matrix3x2_one():
    matrix3x2_one = Matrix(3, 2)
    matrix3x2_one.fill_row(1, [3, 5, 10, 45])
    matrix3x2_one.fill_row(2, [1, 2, 3, 4, 5, 6, 7])
    matrix3x2_one.fill_row(3, [4, 5, 6, 7])
    return matrix3x2_one


@pytest.fixture
def matrix3x2_double():
    matrix3x2_double = Matrix(3, 2)
    matrix3x2_double.fill_row(1, [3, 5])
    matrix3x2_double.fill_row(2, [1, 2])
    matrix3x2_double.fill_row(3, [4, 5])
    return matrix3x2_double


@pytest.fixture
def matrix3x2_other():
    matrix3x2_other = Matrix(3, 2)
    matrix3x2_other.fill_row(1, [3, 4])
    matrix3x2_other.fill_row(2, [1, 6])
    matrix3x2_other.fill_row(3, [0, 5])
    return matrix3x2_other


@pytest.fixture
def summ_matrix3x2():  # matrix3x2_one + matrix3x2_other
    summ_matrix3x2 = Matrix(3, 2)
    summ_matrix3x2.fill_row(1, [6, 9])
    summ_matrix3x2.fill_row(2, [2, 8])
    summ_matrix3x2.fill_row(3, [4, 10])
    return summ_matrix3x2


@pytest.fixture
def other_matrix():
    other_matrix = Matrix(2, 3)
    other_matrix.fill_row(1, [2, 5, 69, 46])
    other_matrix.fill_row(2, [1, 2, 3, 4, 5, 6, 7])
    return other_matrix


def test_equal_valid(matrix3x2_one, matrix3x2_double):
    assert (matrix3x2_one == matrix3x2_double) is True


def test_equal_non_valid(matrix3x2_one, matrix3x2_other):
    assert (matrix3x2_one == matrix3x2_other) is False


def test_equal_different_size_valid(matrix3x2_one, other_matrix, capfd):
    eggs = matrix3x2_one == other_matrix
    msg = capfd.readouterr()
    assert msg.out == 'размеры матриц: (3x2) и (2x3) не совпадают. операция "сравнение" не может быть выполнена\n'


def test_non_equal_valid(matrix3x2_one, matrix3x2_other):
    assert (matrix3x2_one != matrix3x2_other) is True

def test_non_equal_different_size_valid(matrix3x2_one, other_matrix, capfd):
    eggs = matrix3x2_one == other_matrix
    msg = capfd.readouterr()
    assert msg.out == 'размеры матриц: (3x2) и (2x3) не совпадают. операция "сравнение" не может быть выполнена\n'


def test_summ_valid(matrix3x2_one, matrix3x2_other, summ_matrix3x2):
    eggs = (matrix3x2_one + matrix3x2_other)
    assert (eggs == summ_matrix3x2) is True

def test_summ_non_valid(matrix3x2_one, matrix3x2_other):
    eggs = (matrix3x2_one + matrix3x2_other)
    assert (eggs == matrix3x2_one) is False




if __name__ == "__main__":
    pytest.main(['-v'])
