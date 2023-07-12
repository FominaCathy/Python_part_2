'''
2. Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
'''

my_list = ['astra', True, 2, 6, True, 'astra', 6, 12, 'e', 6]
NOT_DUBLE = 1
new_list = []
for item in set(my_list):
    if my_list.count(item) > NOT_DUBLE:
        new_list.append(item)

print(new_list)
