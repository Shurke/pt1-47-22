'''
2. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
'''


my_str = input('Please enter string text: ')
import re
words = re.split('[- ,: ; .""'']', my_str)
l = 0
for index in range(len(words)):
    if len(words[index]) > len(words[l]):
        l = index
print(words[l])



