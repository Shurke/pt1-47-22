"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""

import string

str_in = input('Введите строку: ')
symbal_str = 0
symbal_prop = 0
for char in str_in:
    if char in string.ascii_lowercase:
        symbal_str += 1
    elif char in string.ascii_uppercase:
        symbal_prop += 1
print(f'Количество строчный английских букв в строке: {symbal_str} \n'
      f'Количество прописных английских букв в строке: {symbal_prop}')
