"""
2. List practice
1. Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий:
['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий:
['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент '2a' из прошлого списка и
напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a' так чтобы в
исходном списке этого элемента не было.
"""


import copy

list1 = [i for i in ('ab', 'ac', 'ad', 'bb', 'bc', 'bd')]
print(list1)

new_list1 = list1[0:5:2]
print(new_list1)

list2 = [i for i in ('1a', '2a', '3a', '4a')]
print(list2)

print(list2.pop(1))

list2_copy = copy.deepcopy(list2)
list2_copy.append('a2')
print(list2_copy)
