'''
(Задача 4)
📌 Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
   идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
📌 Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
📌 Отдельно напишите функцию, которая считывает информацию
   из JSON файла и формирует множество пользователей.
'''

import json
from pathlib import Path


class Person:

    def __init__(self, name, num_id, level):
        self.name = name
        self.num_id = num_id
        self.level = level

    def __str__(self):
        return f'name: {self.name}, id: {self.num_id}, level: {self.level}'

    def __eq__(self, other):
        return (self.num_id == other.num_id) and (self.name == other.name)


def create_file_data(file: Path):
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


def convert_to_set_person(file: Path) -> set():
    person_set = set()

    try:
        with open(file, 'r', encoding='utf-8') as fj:
            dict_bd = json.load(fj)

        for level, subdict in dict_bd.items():
            for id_cod, name in subdict.items():
                person_set.add(Person(name, id_cod, level))

    except FileNotFoundError as exp:
        print(f'not file open: {exp}')

    return person_set


if __name__ == '__main__':

    data_person = set()
    data_person = convert_to_set_person('../Exception_13/test_bd.json')

    for item in data_person:
        print(item)
