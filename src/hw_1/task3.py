""""""
3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""


str_input = input('Введите строку: ')
result = ''
for c in range(len(str_input)):
    if result.find(str_input[c]) == -1 and str_input[c] != ' ':
        result += str_input[c]
print(result)
