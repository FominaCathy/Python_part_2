'''

Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''

path_absolut: str = 'C:\\Program Files\\Charles\\extra\\Run Charles.bat'

*path_file, name_file = path_absolut.split('\\')

spam: tuple = (str("/".join(path_file)+'/'), name_file.split('.')[0], name_file.split('.')[1])
print(spam)
