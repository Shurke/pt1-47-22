"""
3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. Например, если
было введено "abc cde def", то должно быть выведено "abcdef".
"""


STR_1 = input('Исходная строка: ')
TRASH = ' '
STR_2 = ''

for char in STR_1:
    if char not in TRASH:
        STR_2 += char
        TRASH += char

print(f'Чистая строка: {STR_2}')
