"""
3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. Например, если
было введено "abc cde def", то должно быть выведено "abcdef".
"""


str_1 = input('Исходная строка: ')
trash = ' '
str_2 = ''

for char in str_1:
    if char not in trash:
        str_2 += char
        trash += char

print(f'Чистая строка: {str_2}')
