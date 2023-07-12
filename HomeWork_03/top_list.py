'''
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
'''

import re
import text_for_task as txt

string_wiki: str = txt.text

delimiters = ';|, |:|\\. |\\ |\\-|\\(|\\)|\\«|\\»|\\&|\\.|\\n|\\!|\\?'

TOP_COUNT = 10

string_list = re.split(delimiters, string_wiki.lower())

my_dict = dict()
for item in set(string_list):
    if len(item) > 0:
        my_dict[item] = string_list.count(item)

result_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

for i in range(0, TOP_COUNT):
    print(f'{i + 1}. {result_dict[i][0]} - {result_dict[i][1]} раз/раза')
