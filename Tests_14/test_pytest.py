import pytest
from prime import is_prime


def sum_two_num(a, b):
    return a + b


def test_sum():
    assert sum_two_num(2, 3) == 5, 'Математика покинула чат'


def test_is_prime():
    assert not is_prime(6)
    assert is_prime(7)


def test_warning_false(capfd):
    is_prime(100_000_001)

    captured = capfd.readouterr()
    assert captured.out == 'If the number P is prime, the check may take a long time.Working...\n'


if __name__ == '__main__':
    pytest.main(['-v'])
