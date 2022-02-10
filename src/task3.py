"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef"
"""

str_ = input('Введите строку:')
str_ = str_.replace(' ', '')
s_new = ''
for i in str_:
    if i not in s_new:
        s_new = s_new + i
print('Результат:', s_new)
