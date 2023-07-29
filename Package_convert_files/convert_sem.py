import csv
import json
from pathlib import Path

__all__ = ['convert_json_to_csv', 'convert_csv_to_json']

'''
Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.
'''


def create_json(file: Path):
    dict_data = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split(' ')
            dict_data[name.title()] = float(number)
        with open(f'{file.name}.json', 'w') as fj:
            json.dump(dict_data, fj, indent=2)


'''
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7). 
После каждого ввода добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа. 
Идентификатор пользователя выступает ключём для имени. 
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. 
При перезапуске функции уже записанные в файл данные должны сохраняться.
'''


def fill_bd(file: Path):
    current_set = set()

    if Path.exists(file):
        with open(file, 'r', encoding='utf-8') as fj:
            dict_bd = json.load(fj)
            for _, value in dict_bd.items():
                current_set.update(value.keys())
    else:
        dict_bd = {str(i): {} for i in range(1, 8)}

    current_data = input(f'введите Имя, id, уровень доступа (от 1 до 7) через пробел: \n ')
    while current_data != "":
        name, id_cod, level = current_data.split()

        if id_cod not in current_set:
            current_set.add(id_cod)
            dict_bd[level][id_cod] = name

            with open(file, "w", encoding='utf-8') as fj:
                json.dump(dict_bd, fj, indent=2, ensure_ascii=False)

        current_data = input(f'введите Имя, id, уровень доступа (от 1 до 7) через пробел: \n ')


'''
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
'''


def convert_json_to_csv(file: Path):
    with (open(file, 'r', encoding='utf-8') as fj,
          open(f'{file.name}.csv', 'w', encoding='utf-8', newline='') as fc):

        spam = json.load(fj)
        temp_list = []
        for level, value in spam.items():
            for id_cod, name in value.items():
                temp_list.append({'level': int(level), 'id_cod': id_cod, 'name': name})

        csv_temp = csv.DictWriter(fc, dialect='excel', fieldnames=['level', 'id_cod', 'name'])
        csv_temp.writeheader()
        csv_temp.writerows(temp_list)


'''
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной. 
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь. 
Имя исходного и конечного файлов передавайте как аргументы функции.
'''


def convert_csv_to_json(csv_file, json_file):
    with (open(csv_file, 'r', encoding='utf-8') as fc,
          open(json_file, 'w', encoding='utf-8') as fj):
        file = list(csv.reader(fc, dialect='excel'))

        lst = []
        for i, item in enumerate(file):
            if i == 0:
                h_level, h_id, h_name = item
            else:
                lst.append(({h_level: item[0], h_id: item[1].zfill(10), h_name: item[2].title(),
                             'hash': hash(item[2] + item[0])}))
        json.dump(lst, fj, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # create_json('result.txt')
    # fill_bd(Path('test_bd.json'))
    # convert_json_to_csv('test_bd.json')
    convert_csv_to_json('test_files/test_bd.csv', 'test_files/new_test_bd.json')
