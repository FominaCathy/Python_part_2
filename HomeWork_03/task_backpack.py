'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
'''

dict_items = {'спальник': 2, 'котелок': 3, 'спички': 7, 'палатка': 17, 'фонарик': 2, 'вода': 1, 'стул': 8}
# dict_items = {'спальник': 12, 'котелок': 1, 'спички': 7, 'палатка': 17, 'фонарик': 6, 'вода': 5, 'стул': 7}

SIZE_BACKPACK = 10
list_items_var = list()
list_all_items = list(dict_items.keys())
count_items = len(list_all_items)
list_all_backpack = []


def all_valid_set(current_size, current_list, start, list_all: list) -> list:
    for item in range(start, count_items):

        size = dict_items.get(list_all_items[item])
        if (current_size < SIZE_BACKPACK) and (SIZE_BACKPACK - current_size) >= size:
            current_size += size
            list_items_var.append(list_all_items[item])

        if current_size == SIZE_BACKPACK:
            list_all.append(tuple([current_size, tuple(list_items_var)]))
            list_items_var.pop()
            current_size -= size

    if len(list_items_var) != 0:
        list_all.append(tuple([current_size, tuple(list_items_var)]))
        remove_element = list_items_var.pop()
        next_start = list_all_items.index(remove_element) + 1
        current_size -= dict_items.get(remove_element)
        all_valid_set(current_size, current_list, next_start, list_all)

    return list_all


all_var: list = sorted(all_valid_set(0, list_items_var, 0, list_all_backpack), key=lambda x: x[0], reverse=True)

print(f'любой вариант (вес = {all_var[0][0]}ед):\t {all_var[0][1]}')
if min(list(dict_items.values())) > SIZE_BACKPACK:
    print("все вещи по весу больше чем рюкзак")
elif sum(list(dict_items.values())) <= SIZE_BACKPACK:
    print("все вещи поместятся рюкзак")
else:
    print(f'\nмаксимально возможные варианты загрузки (на {all_var[0][0]} ед):')
    i = 0
    while all_var[i][0] == all_var[0][0]:
        print(all_var[i][1])
        i += 1
