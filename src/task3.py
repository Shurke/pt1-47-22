"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef"
"""

str_ = input('Введите строку:')
str_ = str_.replace(' ', '')
S_NEW = ''
for i in str_:
    if i not in S_NEW:
        S_NEW = S_NEW + i
print('Результат:', S_NEW)
