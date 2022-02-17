""" Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""

import string

a = input('Введите предложение: ')
upper = 0
lower = 0

for i in a:
    if i in string.ascii_uppercase:
        upper += 1
    if i in string.ascii_lowercase:
        lower += 1

print('Прописных: ', upper, 'Строчных: ', lower)
