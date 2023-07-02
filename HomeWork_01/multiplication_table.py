'''
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

'''
print("ТАБЛИЦА УМНОЖЕНИЯ".center(62))
for i in range(0, 2):
    for j in range(2, 11):
        for k in range(2 + i * 4, 6 + i * 4):
            print(f'{k:2} * {j:2} = {j * k:2} \t', end='')
        print('')
    print()
