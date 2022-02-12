""" Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке """

import re

sen = input("Enter your sentence: ")
new_sen = re.sub(r'[^\w\s]','', sen)
new_sen = new_sen.split()
x = len(new_sen)
word = 0
i = 0
while x > 0:
    if len(new_sen[i]) > len(new_sen[word]):
        word = i
    i += 1
    x -= 1
print("longest word in your sentence - ", new_sen[word])
