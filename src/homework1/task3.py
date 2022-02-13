"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""


string = input('Введите строку: ')
new_string = string.split()                      # split string by spaces
new_string = ''.join(new_string)                 # concatenate a list into a string without spaces
res = ''                                         # create new empty string
for i in new_string:                             # loop through the characters in a string
    if i not in res:                             # if no characters in list
        res += i                                 # add to new string

print(res)
