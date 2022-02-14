import copy

"""Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
"""

str_1 = 'ab'
str_2 = 'bcd'

spisok = [i + f for i in str_1 for f in str_2]
print(spisok)

'''Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].'''

spisok_2 = spisok[::2]
print(spisok_2)

'''Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].'''

a = 'a'
spisok_3 = [a + str(i) for i in range(1, 5)]
print(spisok_3)

'''Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.'''

elem = spisok_3.pop(1)
print(elem)

'''Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента
не было.'''

a = copy.copy(spisok_3)
a.append(elem)
print(a)