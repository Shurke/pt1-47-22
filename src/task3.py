"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

pred = input("Введите предложение: ")
SR_R = pred.split()
DGO = ("".join(SR_R))
RE = ""
for char in DGO:
    if char not in RE:
        RE = RE + char
print("Полученная строка: ", RE)
