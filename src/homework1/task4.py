"""
4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""


import string

STR_1 = input('Исходная строка: ')
BIG_COUNT = 0
SMALL_COUNT = 0

for CHAR in STR_1:
    if CHAR in string.ascii_uppercase:
        BIG_COUNT += 1
    elif CHAR in string.ascii_lowercase:
        SMALL_COUNT += 1

print(f'Заглавных английских букв {BIG_COUNT}, а строчных - {SMALL_COUNT}!')
