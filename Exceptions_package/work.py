"""
📌 Создайте функцию, которая запрашивает числовые данные от
   пользователя до тех пор, пока он не введёт целое или вещественное число.
📌 Обрабатывайте не числовые данные как исключения.
"""


def input_num() -> float:
    while True:
        try:
            spam = float(input('введите целое или вещественное число \n'))

        except ValueError as exp:
            print(f"введены данные неправльногоо типа: {exp}")

        else:
            return spam


"""
📌 Создайте функцию аналог get для словаря.
📌 Помимо самого словаря функция принимает ключ и значение по умолчанию.
📌 При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
📌 Реализуйте работу через обработку исключений.
"""


def get_value(diction: dict, key, value_defolt=None):
    try:
        spam = diction[key]
    except KeyError as exp:
        spam = value_defolt

    return spam


if __name__ == "__main__":
    # print(input_num())

    eggs_dict = {'one': 1, 'two': 2, 'char': 'k'}

    print(get_value(eggs_dict, 'two'))
    print(get_value(eggs_dict, 'two', 'err'))
    print(get_value(eggs_dict, 'two222', 'err'))
    print(get_value(eggs_dict, 'two222'))
