"""
List practice
Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так
чтобы в исходном списке этого элемента не было.
"""


import copy

first_list = [x + y for x in 'ab' for y in 'bcd']
print(first_list)
print(first_list[::2])

sec_list = [z + 'a' for z in '1234']
print(sec_list)
print(sec_list.pop(1))

thrd_list = copy.deepcopy(sec_list)
thrd_list.insert(1, '2a')
print(thrd_list)
