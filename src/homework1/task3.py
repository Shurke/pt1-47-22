"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""


string = input('Введите строку ')
new_string = string.split()                      # split string by spaces
new_string = ''.join(new_string)                 # concatenate a list into a string without spaces
res = []                                         # create new empty list
for i in new_string:                             # loop through the characters in a string
    if i not in res:                             # if no characters in list
        res.append(i)                            # add to new list

res = ''.join(res)                               # create a string from a list
print(res)
