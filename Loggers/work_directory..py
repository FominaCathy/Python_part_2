'''
Задание №6
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.

'''
import argparse
import logging
from pathlib import Path
import os
from collections import namedtuple


def content(path):
    Elem = namedtuple('Elem', ['name', 'exp', 'flag_dir', 'parent_dir'])
    list_elem = list()
    try:
        os.chdir(path)
        for dir_path, dir_name, file_name in os.walk(path):
            print(f'{dir_path} - {dir_name} - {file_name}')
            for dir_item in dir_name:
                list_elem.append(Elem(dir_item, "", True, dir_path))
            for file_item in file_name:
                list_elem.append(Elem(Path(file_item).stem, Path(file_item).suffix, False, dir_path))
                logger.info(Elem(Path(file_item).stem, Path(file_item).suffix, False, dir_path))
    except Exception as ex:
        logger.error(f'что-то пошло не так...: {ex}')
        print(f'что-то пошло не так...: {ex}')


if __name__ == '__main__':
    logging.basicConfig(filename='path_logger.log', filemode='w', encoding='utf-8', level=logging.NOTSET)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='my')
    parser.add_argument('cur_path', metavar='p', type=str, default="", help='введите путь до директории')

    current_path = parser.parse_args()

    content(current_path.cur_path)
    # content('../Folder_for_HW09')
