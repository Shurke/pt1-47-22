"""
Анаграммами называются слова, образованные путем взаимной перестановки букв.
В английском языке, например, анаграммами являются слова «live» и «evil», а в
русском – «выбор» и «обрыв». Напишите программу, которая будет запрашивать у
пользователя два слова, определять, являются ли они анаграммами, и выводить на
экран ответ.
1-й вариант:

lst_1 = input("Введите первое слово: ").lower()
lst_2 = input("Введите второе слово: ").lower()

key_1 = set(lst_1)
rez_1 = dict.fromkeys(key_1, 0)
for key_1 in lst_1:
    rez_1[key_1] += 1

key_2 = set(lst_2)
rez_2 = dict.fromkeys(key_2, 0)
for key_2 in lst_2:
    rez_2[key_2] += 1

if rez_1 == rez_2:
    print(f"Слова {lst_1} и {lst_2} анаграммы.")
else:
    print(f"Слова {lst_1} и {lst_2} не анаграммы.")

2-й вариант:
"""

import collections

lst_1 = input("Введите первое слово: ").lower()
lst_2 = input("Введите второе слово: ").lower()
counter_1 = collections.Counter(lst_1)
counter_2 = collections.Counter(lst_2)
if counter_1 == counter_2:
    print(f"Слова {lst_1} и {lst_2} анаграммы.")
else:
    print(f"Слова {lst_1} и {lst_2} не анаграммы.")
