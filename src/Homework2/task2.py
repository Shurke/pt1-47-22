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

lis = [x + y for x in "ab" for y in "bcd"]
print(lis)
lis = lis[::2]
print(lis)
new_lis = [x + y for x in "1234" for y in "a"]
print(new_lis)
print(new_lis.pop(1))
print(new_lis)
lis_cop = copy.deepcopy(new_lis)
lis_cop.insert(1, "2a")
print(lis_cop)
print(new_lis)
