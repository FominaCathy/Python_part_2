# Три друга взяли вещи в поход.
# Сформируйте словарь, где ключ - имя друга,
# а значение - кортеж вещей. Ответьте на вопросы:
#     какие вещи взяли все три друга
#     какие вещи уникальны, есть только у одного друга
#     какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
#
# Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.


def get_all_items(friends_items) -> set():  # список всех вещей
    all_items = set()

    for item in friends_items.values():
        all_items.update(item)

    return all_items


def get_common_items(friends_items) -> set():  # какие вещи взяли все три друга
    all_items = get_all_items(friends_items)

    common_items = set()
    common_items.update(all_items)
    for item in friends_items.values():
        common_items = common_items.intersection(item)

    return common_items


def get_unique_items(friends_items: dict) -> set():  # какие вещи уникальны, есть только у одного друга
    unique_items = set()
    double_items = set()

    for item in friends_items.values():
        if len(unique_items) == 0:
            unique_items.update(set(item))
        else:
            double_items.update(set.intersection(unique_items, item))
            unique_items.update(item)
            unique_items.difference_update(double_items)

    return unique_items


def get_other_items(friends_items) -> set:
    # какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
    other_items = set()
    all_items = get_all_items(friends_items)
    common_items = get_common_items(friends_items)
    unique_items = get_unique_items(friends_items)
    other_items = all_items.difference(common_items, unique_items)

    none_items = set(tuple())
    for element in other_items:
        for friend in friends_items.items():
            if element not in set(friend[1]):
                none_items.add((element, friend[0]))

    return none_items


friends_items = {
    'Вася': ('Рюкзак', 'Палатка', 'Спальник', 'Фонарик', 'Кружка'),
    'Петя': ('Рюкзак', 'Палатка', 'Котелок', 'Кружка', 'Спички'),
    'Марик': ('Рюкзак', 'Палатка', 'Спички', 'Складной стул')
}

print(f'\nвещи, которые есть у каждого друга: {get_common_items(friends_items)}\n')
print(f'уникальные вещи, есть только у одного друга: {get_unique_items(friends_items)}\n')

print(f'вещи есть у всех друзей кроме одного друга и имя того, у кого данная вещь отсутствует:')

current_list = get_other_items(friends_items)
for item in current_list:
    print(f'{item[0]} - отсутствует у {item[1]}')
