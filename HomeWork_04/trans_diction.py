'''
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где
ключ — значение переданного аргумента, а
значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
'''


# реализация 1
def function_free(**kwargs):
    tranc_dict = dict()
    non_hash_types: set = {int, float, complex, bool, str, tuple, range, frozenset, bytes}
    spam = iter(kwargs.items())
    for key, value in spam:
        if type(value) in non_hash_types:
            tranc_dict[value] = key
        else:
            tranc_dict[str(value)] = key

    return tranc_dict


# реализация 2
def function_free_new(**kwargs):
    non_hash_types: set = {int, float, complex, bool, str, tuple, range, frozenset, bytes}
    tr_dict: dict = {value if type(value) in non_hash_types else str(value): key for key, value in kwargs.items()}

    return tr_dict


print(function_free(a=5, r=3.14, flag=True, s=(2, 3, 6), l=[1, 2, 0]))
print(function_free_new(a=5, r=3.14, flag=True, s=(2, 3, 6), l=[1, 2, 0]))
