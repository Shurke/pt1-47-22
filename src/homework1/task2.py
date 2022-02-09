"""
2. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
"""


string = input('Введите строку: ')
signs = [';', ',', '.', ':', '!', '?']

for char in string:
    if char in signs:
        string = string.replace(char, ' ')

print(max(string.split(), key=len))
