'''
Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
'''

import csv


class ExceptionBase(Exception):
    pass


class UserNameNotTitle(ExceptionBase):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Имя '{self.value}' - должно начинаться с большой буквы."


class UserNameNotIsAlpha(ExceptionBase):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Имя '{self.value}' - не может содержать символы отличные от букв."


class ValueNotDiapazon(ExceptionBase):

    def __init__(self, name_param, subject, min_value, max_value):
        self.name_param = name_param
        self.min_value = min_value
        self.max_value = max_value
        self.subject = subject

    def __str__(self):
        return f'{self.name_param} по предмету {self.subject} должна/ен быть в диапазоне от {self.min_value} до {self.max_value}'


class Validname:

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return self.name

    def __set__(self, instance, value: str):

        if not value.isalpha():
            raise UserNameNotIsAlpha(value)
        if not value.istitle():
            raise UserNameNotTitle(value)

        self.name = value



class Student:
    name = Validname('name')
    surname = Validname('surname')
    _subject = dict()
    list_score = []

    MIN_SCORE = 2
    MAX_SCORE = 5
    MIN_TEST = 0
    MAX_TEST = 100

    def __init__(self, name, surname, file_subject):

        self.name = name
        self.surname = surname
        self.list_score = []

        try:
            with open(file_subject, 'r', newline='') as fc:
                csv_reader = csv.reader(fc, dialect='excel')
                for row in csv_reader:
                    for item in row:
                        self._subject[item] = {'score': [], 'tests': []}
        except FileNotFoundError as exp:
            print(f'указанный файл не существует: {exp}')

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __call__(self, subject, score=None, test=None):

        try:
            if score and (self.MAX_SCORE >= score >= self.MIN_SCORE):
                self._subject[subject]['score'].append(score)
                self.list_score.append(score)
            elif score:
                raise ValueNotDiapazon('оценка', subject, self.MIN_SCORE, self.MAX_SCORE)

            if test and (self.MAX_TEST >= test >= self.MIN_TEST):
                self._subject[subject]['tests'].append(test)
            elif test:
                raise ValueNotDiapazon('результат теста', subject, self.MIN_TEST, self.MAX_TEST)

        except KeyError as exp:
            print(f'ERROR: not subject {exp}')

        except ExceptionBase as eb:
            print(eb)

    @property
    def average_score(self):
        # средний балл по по оценкам всех предметов вместе взятых
        if len(self.list_score) > 0:
            return sum(self.list_score) / len(self.list_score)
        else:
            return 0

    def average_test(self, subject=None):
        # средний балл по тестам для каждого предмета
        try:
            spam = self.subject[subject]['tests']
            return sum(spam) / len(spam)
        except Exception as exp:
            print('не указан предмет')

    @property
    def subject(self):
        return self._subject


def fill_file_subject(name_file):
    list_subject = ["algebra", 'chemistry', 'physics', 'ecology', 'TFCV', 'herbology']
    with open(name_file, 'w', encoding='utf-8', newline='') as fc:
        csv_writer = csv.writer(fc)
        csv_writer.writerow(list_subject)


if __name__ == '__main__':
    file_subject = 'subject.csv'
    fill_file_subject(file_subject)
    ivan = Student("Ivan", 'Doin', file_subject)
    ivan('algebra', score=15, test=69)
    ivan('algebra', test=59)
    ivan('algebra', score=2)
    ivan('physics', score=5, test=198)
    ivan('herbology', score=2, test=100)
    ivan('herbology', score=5, test=98)

    print(f'\nданные студента {ivan.name}')
    for key, value in ivan.subject.items():
        print(f'{key} - {value}')
    spam = 'algebra'
    print(f'\naverage TEST on {spam} = {ivan.average_test(spam)}')

    print(f'\naverage score {ivan}: {ivan.average_score}')
