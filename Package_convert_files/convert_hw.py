'''
Задачи из дом. задания (ДЗ)
'''
import csv
import json
import os
from pathlib import Path
import pickle

__all__ = ['convert_json_to_pickle', 'convert_pickle_to_csv', 'group_convert_json_to_pickle']

'''
№ 5 (ДЗ) Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
'''


def convert_json_to_pickle(file_json: Path):
    file_pickle = Path(file_json).with_suffix('.pickle')

    with (open(file_json, 'r', encoding='utf-8') as fj,
          open(file_pickle, 'wb') as fp):
        current_dir = json.load(fj)
        pickle.dump(current_dir, fp)


def group_convert_json_to_pickle(folder: Path):
    if folder != "":
        os.chdir(folder)

    for item in os.listdir():
        if os.path.isfile(item) and Path(item).suffix == '.json':
            convert_json_to_pickle(Path(item))


'''
№ 6 (ДЗ) Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 5 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
'''


def convert_pickle_to_csv(file_pickle: Path):
    file_csv = Path(file_pickle).with_suffix('.csv')

    with (open(file_pickle, 'rb') as fp,
          open(file_csv, 'w', newline='', encoding='utf-8') as fc):
        dict_spam = pickle.load(fp)

        csv_spam = csv.DictWriter(fc, dialect='excel', fieldnames=dict_spam[0].keys())
        csv_spam.writeheader()
        csv_spam.writerows(dict_spam)


'''
№ 7 (ДЗ) Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку.
'''


def reader_csv(file_csv: Path):
    with open(file_csv, 'r', encoding='utf-8', newline='') as fc:
        csv_spam = list(csv.reader(fc, dialect='excel'))
        list_dict = []
        header_spam = []
    for i, line in enumerate(csv_spam):
        if i == 0:
            header_spam.extend(line)
        else:
            list_dict.append({header: value for header, value in zip(header_spam, line)})

    pickle_spam = str(pickle.dumps(list_dict))
    print(pickle_spam)


if __name__ == "__main__":
    # convert_json_to_pickle('FOLDER_01/test_bd.json')
    # group_convert_json_to_pickle('FOLDER_01')
    # convert_pickle_to_csv('FOLDER_01/new_test_bd.pickle')
    reader_csv('test_files/new_test_bd.csv')
