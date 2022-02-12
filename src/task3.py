"""
3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

s = input('Please enter string text: ')
s_new = ''
for i in s:
    if i not in s_new and i != ' ':
        s_new += i
print(s_new)
