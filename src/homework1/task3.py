"""
3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""


string = input('Введите строку: ')
new_string = ' '

for char in string:
    if char not in new_string:
        new_string += char

print(new_string.strip())
