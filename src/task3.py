"""
3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

s = input('Please enter string text: ')
S_NEW = ''
for i in s:
    if i not in S_NEW and i != ' ':
        S_NEW += i
print(S_NEW)
