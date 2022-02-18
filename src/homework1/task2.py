"""
2. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
"""


import string

user_string = input('Введите строку: ')

for char in user_string:
    if char in string.punctuation:
        user_string = user_string.replace(char, ' ')

print(f'Самое длинное слово в введенном предложении - {max(user_string.split(), key=len)}')
