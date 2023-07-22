'''
4. Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

'''

from chess import check_placement
from itertools import permutations
import random

__all__ = ['generator_placement_queen']

COUNT_PLACEMENT = 4


def generator_placement_queen(max_count=COUNT_PLACEMENT) -> list:
    colons = (1, 2, 3, 4, 5, 6, 7, 8)
    placement_queen = []
    count = 0
    list_placement = list(permutations(range(1, 9)))
    random.shuffle(list_placement)

    for item in list_placement:
        spam = [(col, row) for col, row in zip(colons, item)]
        if check_placement(spam):
            count += 1
            placement_queen.append(spam)
            if count == max_count:
                break
    return placement_queen


if __name__ == "__main__":
    eggs = generator_placement_queen()
    for i, item in enumerate(eggs, 1):
        print(f'вариант расстановки {i}: {item}')
