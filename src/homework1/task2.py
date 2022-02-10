"""
2. Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки
препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
"""


import string

STR_1 = (input('Исходная строка: '))
STR_2 = ''
BEST_WORD = ''
BEST_WORD_LENGTH = 0

for CHAR in STR_1:
    if CHAR not in string.punctuation:
        STR_2 += CHAR
    else:
        STR_2 += ' '

LIST_S = STR_2.split()
for SMALL_STR in LIST_S:
    if len(SMALL_STR) > BEST_WORD_LENGTH:
        BEST_WORD = SMALL_STR
        BEST_WORD_LENGTH = len(SMALL_STR)

print(f'Самое длинное слово - это "{BEST_WORD}" с количеством букв, равным {BEST_WORD_LENGTH}')
