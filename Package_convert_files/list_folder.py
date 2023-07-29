'''
2.Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

'''

from pathlib import Path
import os
import json
import pickle
import csv

__all__ = ['get_list_folder', 'write_to_files']


def get_list_folder(folder: Path) -> list:
    if folder != '':
        os.chdir(folder)

    list_folder = list()

    for item in os.walk(os.getcwd(), topdown=False):

        list_folder.extend(
            [[item[0], 'FILE', curr_file, os.path.getsize(f'{item[0]}/{curr_file}')] for curr_file in item[2]])

        for curr_folder in item[1]:
            curr_path = os.path.join(item[0], curr_folder)  #
            sum_folder = 0
            for elm in list_folder:
                if elm[0] == curr_path:
                    sum_folder += int(elm[3])
            list_folder.append([item[0], 'DIR', curr_folder, sum_folder])

    header = ['folder_parent', 'type_obj', 'name_obj', 'size']
    dict_folder = []

    for item in list_folder:
        dict_folder.append({header: value for header, value in zip(header, item)})

    return dict_folder


def write_to_files(list_data: list, path_file: Path, file_name):
    if path_file != '':
        os.chdir(path_file)

    with (open(f'{file_name}.csv', 'w', encoding='utf-8', newline='') as fc,
          open(f'{file_name}.json', 'w', encoding='utf-8', ) as fj,
          open(f'{file_name}.pickle', 'wb') as fp):
        csv_spam = csv.DictWriter(fc, dialect='excel', fieldnames=list_data[0].keys())
        csv_spam.writeheader()
        csv_spam.writerows(list_data)

        json.dump(list_data, fj, ensure_ascii=False, indent=2)
        pickle.dump(list_data, fp)


if __name__ == '__main__':
    list_folder_spam = get_list_folder('../Folder_for_HW09')
    write_to_files(list_folder_spam, '../Folder_for_HW09', 'list_dir')
