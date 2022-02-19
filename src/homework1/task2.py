"""Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки
препинания.
"""

import string

sen = input('Введите предложение: ').translate(str.maketrans('', '', string.punctuation)).split(' ')
a = 0
sen_2 = None
for i in sen:
    if len(i) >= a:
        a += len(i)
        sen_2 = i
print('Самое длинное слово в предложении: ', sen_2)
