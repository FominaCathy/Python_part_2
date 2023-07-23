
import random
from random import randint, uniform, shuffle

MIN_NUM = -1000
MAX_NUM = 1000
STR_CHAR = 'qwrtpsdfghjklzxcvbnm'
STR_VOWEL = 'eyuioa'
MIN_LEN_PS = 4
MAX_LEN_PS = 7

__all__ = ['generator_pairs_number', 'generator_psevdonim', 'fill_file_result']
'''
Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.
'''


def generator_pairs_number(count: int, name_file: str):
    with open(name_file, 'a', encoding='utf-8') as f:
        for i in range(0, count):
            f.write(f'{randint(MIN_NUM, MAX_NUM)} | {uniform(MIN_NUM, MAX_NUM)}\n')


'''
Напишите функцию, которая генерирует псевдоимена. 
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные. 
Полученные имена сохраните в файл.

'''

'''
Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами. 
Перемножьте пары чисел. В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле. 
При достижении конца более короткого файла, возвращайтесь в его начало.
'''


def fill_file_result(file_nums: str, file_psew: str, file_res: str):
    with (
        open(file_nums, 'r', encoding='utf-8') as f_nums,
        open(file_psew, 'r', encoding='utf-8') as f_psew,
        open(file_res, 'w', encoding='utf-8') as f_res
    ):
        f_psew_len = len(f_psew.readlines())
        f_nums_len = len(f_nums.readlines())

        for i in range(0, max(f_nums_len, f_psew_len)):
            spam = f_nums.readline().strip()
            eggs = f_psew.readline().strip()
            if not spam:
                f_nums.seek(0)
                spam = f_nums.readline().strip()
            if not eggs:
                f_psew.seek(0)
                eggs = f_psew.readline().strip()

            curr_list = spam.split('|')
            mult = int(curr_list[0]) * float(curr_list[1])

            f_res.write(f'{eggs.lower()} {abs(mult)}\n' if mult < 0 else f'{eggs.upper()} {round(mult)}\n')


def generator_psevdonim(name_file: str):
    spam = random.sample(STR_CHAR, randint(MIN_LEN_PS, MAX_LEN_PS - 1))
    eggs = random.sample(STR_VOWEL, randint(1, len(STR_VOWEL)))
    eggs.extend(spam)
    eggs = eggs[:random.randint(MIN_LEN_PS, MAX_LEN_PS)]
    random.shuffle(eggs)

    with open(name_file, 'a', encoding='utf-8') as f:
        f.write(f'{"".join(eggs).title()}\n')


if __name__ == '__main__':
    # generator_pairs_number(7, 'nums.txt')
    # generator_psevdonim('psew.txt')
    fill_file_result('nums.txt', 'psew.txt', 'result.txt')
