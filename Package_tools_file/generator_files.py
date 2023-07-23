'''
Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
'''
import random
from random import randint
import os

__all__ = ['create_file', 'create_difference_files']

MIN_LEN_NAME = 4
MAX_LEN_NAME = 8
MIN_SIZE = 256
MAX_SIZE = 4096
COUNT_FILE = 42
STR_CHAR = 'qwrtpsdfghjklzxcvbnmeyuioa'


def create_file(exp: str, path="", min_len_name=MIN_LEN_NAME, max_len_name=MAX_LEN_NAME, min_size=MIN_SIZE,
                max_size=MAX_SIZE, count_file=COUNT_FILE):
    for _ in range(0, count_file):
        name_file = "".join(random.choices(STR_CHAR, k=random.randint(min_len_name, max_len_name))) + '.' + exp

        while os.path.exists(name_file):  # если файл с таким именем существует - генерируем новое имя
            name_file = "".join(random.choices(STR_CHAR, k=random.randint(min_len_name, max_len_name))) + '.' + exp

        with open(name_file, 'wb') as f:
            f.write(bytes(randint(0, 255) for _ in range(randint(min_size, max_size))))


'''
Задание №5 (Доработаем предыдущую задачу.)
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
'''
'''
Задание №6 (✔ Дорабатываем функции из предыдущих задач.)
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
'''


def create_difference_files(**kwargs):
    """создание файлов с заданным расщирением и кол-вом
     :param kwargs: расширение=кол-во (напр, txt=6), path=путь к директории в которую создаем файлы.
     если директории нет - она будет создана. по умолчанию - тек. директория
     """
    work_dir = kwargs.get('path')

    if work_dir is not None:
        if not os.path.exists(work_dir):
            os.makedirs(work_dir)
        os.chdir(work_dir)

    for key, value in kwargs.items():
        if key != 'path':
            create_file(key, count_file=value)


if __name__ == '__main__':
    # create_file('txt', count_file=3)
    create_difference_files(path="../Temp/temp1", txt=3, jpg=2, mpeg=3)
