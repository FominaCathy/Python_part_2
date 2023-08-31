"""
Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
    📌 возврат строки без изменений
    📌 возврат строки с преобразованием регистра без потери символов
    📌 возврат строки с удалением знаков пунктуации
    📌 возврат строки с удалением букв других алфавитов
    📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""

import pytest
from function_str import deleter_simbols


def test_no_ch():
    assert deleter_simbols('hello') == 'hello'


def test_Title():
    assert deleter_simbols('Hello') == 'hello'


def test_delete_symbols():
    assert deleter_simbols('hello, kitty!') == 'hello kitty'


def test_delete_rus():
    assert deleter_simbols('hello кат') == 'hello '


def test_all():
    assert deleter_simbols('Hello, кат!') == 'hello '


if __name__ == "__main__":
    pytest.main(['-v'])
