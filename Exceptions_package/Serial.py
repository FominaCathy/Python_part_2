'''
📌 Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
   идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
📌 Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
📌 Отдельно напишите функцию, которая считывает информацию
   из JSON файла и формирует множество пользователей.
'''

import json
from pathlib import Path


class Person:

    def __init__(self, name, numid, level):
        self.name = name
        self.numid = numid
        self.level = level

    def __str__(self):
        return f'name: {self.name}, id: {self.numid}, level: {self.level}'


def fill_bd(file: Path):
    current_set = set()

    if Path.exists(file):
        with open(file, 'r', encoding='utf-8') as fj:
            dict_bd = json.load(fj)
            for _, value in dict_bd.items():
                current_set.update(value.keys())
    else:
        dict_bd = {i: {} for i in range(1, 8)}

        current_data = input(f'введите Имя, id, уровень доступа (от 1 до 7) через пробел: \n ')
        while current_data != "":
            name, id_cod, level = current_data.split()
            if id_cod not in current_set:
                current_set.add(id_cod)
                dict_bd[int(level)] = {id_cod: name}

                with open(file, "w", encoding='utf-8') as fj:
                    json.dump(dict_bd, fj, indent=2, ensure_ascii=False)

            current_data = input(f'введите Имя, id, уровень доступа (от 1 до 7) через пробел: \n ')


def convert_person(file: Path):
    person_set = set()

    try:
        with open(file, 'r', encoding='utf-8') as fj:
            dict_bd = json.load(fj)

        for level, subdict in dict_bd.items():
            for id_cod, name in subdict.items():
                person_set.add(Person(name, id_cod, level))

    except FileNotFoundError as exp:
        print(f'not file open: {exp}')

    for item in person_set:
        print(item)


if __name__ == '__main__':
    #fill_bd(Path('test_bd.json'))
    convert_person('test_bd.json')

