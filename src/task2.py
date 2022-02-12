"""
2. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
"""

import re

my_str = input('Please enter text: ')
words = re.split('[- ,:;."'']', my_str)
str_1 = 0
for i in range(len(words)):
    if len(words[i]) > len(words[str_1]):
        str_1 = i
print(words[str_1])
