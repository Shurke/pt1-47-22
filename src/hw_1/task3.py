"""
3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""


a = input('Введите предложение: ')
b = ''
for c in range(len(a)):
    if b.find(a[c]) == -1 and a[c] != ' ':
        b += a[c]
print(b)
# a - introductory sentence
# b - space
