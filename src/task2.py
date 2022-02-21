"""
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания
"""

import string

STR_ = input('Пожалуйста, введите любое предложение: ')
for i in string.punctuation:
    STR_ = STR_.replace(i, '')
WORD_LIST = STR_.split()
print(max(WORD_LIST, key=len))
