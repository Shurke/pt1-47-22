"""
1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента
не было.
"""


import string

spisok_1 = [item_1 + item_2 for item_1 in string.ascii_lowercase[0:2]
            for item_2 in string.ascii_lowercase[1:4]]
print('Задание 1: ', spisok_1)
print('Задание 2: ', spisok_1[::2])
spisok_2 = [str(item_1) + 'a' for item_1 in range(1, 5)]
print('Задание 3: ', spisok_2)
print('Задание 4: ', spisok_2.pop(1))
spisok_3 = spisok_2[:]
spisok_3.insert(1, '2a')
print('Задание 5:', f'\nИсходный список без "2а": {spisok_2}', f'\nНовый список: {spisok_3}')
