"""Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.
"""

MAIN_LIST = [SPISOK_1 + SPISOK_2 for SPISOK_1 in "ab" for SPISOK_2 in "bcd"]
print(MAIN_LIST)
print(MAIN_LIST[::2])
NEW_LIST = [N_SPISOK_1 + N_SPISOK_2 for N_SPISOK_1 in "1234" for N_SPISOK_2 in "a"]
print(NEW_LIST)
NEW_LIST.remove("2a")
print(NEW_LIST)
NEW_LIST_COPY = NEW_LIST.copy()
NEW_LIST_COPY.insert(1, "2a")
print(NEW_LIST_COPY)
