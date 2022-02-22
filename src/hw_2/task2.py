"""
Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.
"""


import copy

first_list = [first_list + first_list1 for first_list in 'ab' for first_list1 in 'bcd']
print(first_list)
print(first_list[::2])
second_list = [list_sc + 'a' for list_sc in '1234']
print(second_list)
ind = second_list.index('2a')
print(second_list.pop(1))
new_list = copy.deepcopy(second_list)
new_list.insert(ind, '2a')
print(new_list)
