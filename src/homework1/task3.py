#  3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
#  Например, если было введено "abc cde def", то должно быть выведено "abcdef".


text = input('Введите текст: ')
newText = ''

for i in text:
    if i not in newText and i != ' ':
        newText += i
        
print(newText)
