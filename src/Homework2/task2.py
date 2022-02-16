""" 1.Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий:
['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий
['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном
списке этого элемента не было."""

import copy

lis = [lis1 + lis2 for lis1 in "ab" for lis2 in "bcd"]
print("Задание 1:\n", lis)
lis = lis[::2]
print("Задание 2:\n", lis)
new_lis = [lis1 + lis2 for lis1 in "1234" for lis2 in "a"]
print("Задание 3:\n", new_lis)
print("Задание 4:\n", new_lis.pop(1))
print(new_lis)
lis_cop = copy.deepcopy(new_lis)
lis_cop.insert(1, "2a")
print("Задание 5:\n", lis_cop)
print(new_lis)
