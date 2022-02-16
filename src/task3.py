"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

pred = input("Введите предложение: ")
st_r = pred.split()
dgo_n = ("".join(st_r))
re_z = ""
for char in dgo_n:
    if char not in re_z:
        re_z = re_z + char
print("Полученная строка: ", re_z)
