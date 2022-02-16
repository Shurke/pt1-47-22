"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

pred = input("Введите предложение: ")
str = pred.split()
dgon = ("".join(str))
rez = ""
for char in dgon:
    if char not in rez:
        rez = rez + char
print("Полученная строка: ", rez)


