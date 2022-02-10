"""
List practice
Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.
"""


import copy

CHECK_LIST = [LIST_1 + LIST_2 for LIST_1 in 'ab' for LIST_2 in 'bcd']
print(CHECK_LIST)
print(CHECK_LIST[::2])
NEW_CHECK_LIST = [N_LIST_1 + 'a' for N_LIST_1 in '1234']
print(NEW_CHECK_LIST)
INDEX_OF_2A = NEW_CHECK_LIST.index('2a')
print(NEW_CHECK_LIST.pop(NEW_CHECK_LIST.index('2a')))
C_NEW_CHECK_LIST = copy.deepcopy(NEW_CHECK_LIST)
C_NEW_CHECK_LIST.insert(INDEX_OF_2A, '2a')
print(C_NEW_CHECK_LIST)
