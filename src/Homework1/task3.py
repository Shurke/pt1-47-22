""" Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
 Например, если было введено "abc cde def", то должно быть выведено "abcdef". """


sen = input("enter sentence ")
new_sen = " "
for letters in sen:
    if letters not in new_sen:
        new_sen += letters
final = new_sen.split()
print(" ".join(final))
