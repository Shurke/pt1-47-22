""" 2. List practice
a. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
b. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
c. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
d. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
e. Скопируйте список и добавьте в него элемент '2a' так,
чтобы в исходном списке этого элемента не было.
"""


def solution():
    """Реализация решения

    :returns: None
    """
    list_a = [char_a + char_b for char_a in 'ab' for char_b in 'bcd']
    print(f"a. {list_a}")
    list_b = list_a[::2]
    print(f"b. {list_b}")
    list_c = [str(i) + "a" for i in range(1, 5)]
    print(f"c. {list_c}")
    poped_value = list_c.pop(list_c.index('2a'))
    print(f"d. poped value: {poped_value} / list after pop(): {list_c}")
    list_d = list_c[:]
    list_d.append('2a')
    print(f"e. source: {list_c} / copy: {list_d}")


solution()
