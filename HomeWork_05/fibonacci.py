'''
Создайте функцию генератор чисел Фибоначчи
'''


def fibonacci(num: int):
    yield 0
    yield 1
    count = 2
    num_prev = 0
    num_curr = 1
    while count < num:
        num_prev, num_curr = num_curr, (num_prev + num_curr)
        count += 1
        yield num_curr


for i in fibonacci(12):
    print(i, end=', ')
