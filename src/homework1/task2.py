'''Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки
препинания.
'''

import string

a = input().translate(str.maketrans('', '', string.punctuation)).split(' ')
b = 0
c = None
for i in a:
    if len(i) >= b:
        b += len(i)
        c = i
print(c)
