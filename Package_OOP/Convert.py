'''
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.
'''

import csv
import json
from pathlib import Path
import pickle


class FileManager:

    def __init__(self, name: Path):
        self.name = name

    def convert_json_to_pickle(self, name=''):
        """конвертирует файл формата json  в формат pickle. возвращает путь к файлу"""
        file_pickle = Path(self.name).with_suffix('.pickle') if name == '' else name

        with (open(self.name, 'r', encoding='utf-8') as fj,
              open(file_pickle, 'wb') as fp):
            current_dir = json.load(fj)
            pickle.dump(current_dir, fp)
        return Path(file_pickle)

    def convert_json_to_csv(self, name=''):
        """конвертирует файл формата json  в формат csv. возвращает путь к файлу"""
        file_csv = Path(self.name).with_suffix('.csv') if name == '' else name

        with (open(self.name, 'r', encoding='utf-8') as fj,
              open(file_csv, 'w', encoding='utf-8', newline='') as fc):
            spam = json.load(fj)
            heder = spam[0].keys()

            csv_temp = csv.DictWriter(fc, dialect='excel', fieldnames=heder)
            csv_temp.writeheader()
            csv_temp.writerows(spam)

        return Path(file_csv)

    def convert_csv_to_json(self, name=''):
        """конвертирует файл формата csv  в формат json и сохраняет в той-же папке"""
        file_json = Path(self.name).with_suffix('.json') if name == '' else name

        with (open(self.name, 'r', encoding='utf-8') as fc,
              open(file_json, 'w', encoding='utf-8') as fj):
            file = list(csv.reader(fc, dialect='excel'))

            lst = []
            for i, item in enumerate(file):
                if i == 0:
                    heder = item
                else:
                    lst.append(({key: value for key, value in zip(heder, item)}))
            json.dump(lst, fj, ensure_ascii=False, indent=2)

        return Path(file_json)

    def convert_csv_to_pickle(self, name=''):
        """конвертирует файл формата csv  в формат pickle и сохраняет в той-же папке"""
        file_pickle = Path(self.name).with_suffix('.pickle') if name == '' else name

        with (open(self.name, 'r', encoding='utf-8') as fc,
              open(file_pickle, 'wb') as fp):
            curr_file = list(csv.reader(fc, dialect='excel'))

            current_dir = []
            heder = curr_file[0]
            for i, item in enumerate(curr_file):
                if i == 0:
                    continue
                else:
                    current_dir.append(({key: value for key, value in zip(heder, item)}))

            pickle.dump(current_dir, fp)

        return Path(file_pickle)

    def convert_pickle_to_csv(self, name=''):
        """конвертирует файл формата pickle в формат csv и сохраняет в той-же папке"""
        file_csv = Path(self.name).with_suffix('.csv') if name == '' else name

        with (open(self.name, 'rb') as fp,
              open(file_csv, 'w', newline='', encoding='utf-8') as fc):
            dict_spam = pickle.load(fp)

            csv_spam = csv.DictWriter(fc, dialect='excel', fieldnames=dict_spam[0].keys())
            csv_spam.writeheader()
            csv_spam.writerows(dict_spam)

            return Path(file_csv)

    def convert_pickle_to_json(self, name=''):
        """конвертирует файл формата pickle в формат json и сохраняет в той-же папке"""
        file_json = Path(self.name).with_suffix('.json') if name == '' else name

        with (open(self.name, 'rb') as fp,
              open(file_json, 'w', encoding='utf-8') as fj):
            curr_dict = pickle.load(fp)

            json.dump(curr_dict, fj, ensure_ascii=False, indent=2)

        return Path(file_json)


if __name__ == "__main__":
    file_json = FileManager('new_test_bd.json')
    spam_pickle = file_json.convert_json_to_pickle('spam.pickle')
    spam_csv = file_json.convert_json_to_csv('spam.csv')

    file_csv = FileManager('new_test_bd.csv')
    eggs_json = file_csv.convert_csv_to_json('eggs.json')
    eggs_pickle = file_csv.convert_csv_to_pickle('eggs.pickle')

    file_pickle = FileManager('eggs.pickle')
    other_csv = file_pickle.convert_pickle_to_csv('other.csv')
    other_json = file_pickle.convert_pickle_to_json('other.json')
