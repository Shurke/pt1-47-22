"""
4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""


import string

str_1 = input('Исходная строка: ')
big_count = 0
small_count = 0

for char in str_1:
    if char in string.ascii_uppercase:
        big_count += 1
    elif char in string.ascii_lowercase:
        small_count += 1

print(f'Заглавных английских букв {big_count}, а строчных - {small_count}!')
