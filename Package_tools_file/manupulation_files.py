import os

__all__ = ['sort_files_for_dir', 'group_rename_files']

dict_folder = {'mp4': 'Video',
               'mpeg': 'Video',
               'flv': 'Video',
               'txt': 'Text Documents',
               'doc': 'Text Documents',
               'pdf': 'Text Documents',
               'tif': 'Images',
               'rav': 'Images',
               'psd': 'Images',
               'jpg': 'Images'
               }

'''
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки
'''


def sort_files_for_dir(path=""):
    if path != "":
        os.chdir(path)

    list_files = os.listdir()
    for item in list_files:
        if os.path.isfile(item):
            *_, exp_file = item.split('.')
            name_folder = dict_folder.get(exp_file)
            if name_folder is not None:
                if not os.path.exists(name_folder):
                    os.mkdir(name_folder)
                os.replace(item, f'{name_folder}//{item}')


'''
2.Напишите функцию группового переименования файлов. Она должна:
* -- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
* -- принимать параметр количество цифр в порядковом номере.
* -- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
* -- принимать параметр расширение конечного файла.
* -- принимать диапазон сохраняемого оригинального имени. 
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''


def group_rename_files(path='', postfix='', count_digit=4, exp_old='txt', exp_new='', prefix=(1, 3)):
    if path != "":
        os.chdir(path)

    list_files = os.listdir()
    curr_count = 0
    for item in list_files:
        if os.path.isfile(item):
            name_file, exp_file = item.split('.')
            if exp_file == exp_old:
                curr_count += 1
                spam = str(format(curr_count, f'0>{count_digit}'))
                eggs = exp_file if exp_new == "" else exp_new
                new_name = f'{name_file[prefix[0]:prefix[1] + 1]}{postfix}{spam}.{eggs}'

                os.rename(item, new_name)


if __name__ == '__main__':
    # sort_files_for_dir(path="../Temp/temp1")
    group_rename_files(path="../Temp/temp1/Text Documents", postfix='_EEE_', exp_old='txt', exp_new='doc')
