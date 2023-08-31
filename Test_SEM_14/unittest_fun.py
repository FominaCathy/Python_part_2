'''
Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
    📌 возврат строки без изменений
    📌 возврат строки с преобразованием регистра без потери символов
    📌 возврат строки с удалением знаков пунктуации
    📌 возврат строки с удалением букв других алфавитов
    📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
'''

import unittest

from function_str import deleter_simbols


class TestCase(unittest.TestCase):
    def test_no_ch(self):
        self.assertEqual(deleter_simbols('hello'), 'hello')

    def test_Title(self):
        self.assertEqual(deleter_simbols('Hello'), 'hello')

    def test_delete_symbols(self):
        self.assertEqual(deleter_simbols('hello, kitty!'), 'hello kitty')

    def test_delete_rus(self):
        self.assertEqual(deleter_simbols('hello кат'), 'hello ')

    def test_all(self):
        self.assertEqual(deleter_simbols('Hello, кат!'), 'hello ')


if __name__ == '__main__':
    unittest.main(verbosity=2)
