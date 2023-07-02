'''
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
'''

count_row = int(input('введите кол-во рядов елки: '))

for i in range(1, count_row + 1):
    for j in range(0, count_row - i):
        print(' ', end='')
    for j in range(0, i * 2 - 1):
        print('*', end='')
    print('')
