"""
Используя определение подсписка из задачи №8, напишите программу, возвращающую список,
содержащий все возможные подсписки заданного. Например, в число подсписков списка [1, 2, 3] входят
следующие: [], [1], [2], [3], [1, 2], [2, 3] и [1, 2, 3]. Заметьте, что ваша программа должна
вернуть как минимум один пустой список, гарантированно являющийся подсписком для любого списка
"""

LIST_ = [int(i) for i in input('Введите цифры основного списка через пробел: ').split()]
LIST_prt = []
LEN = len(LIST_)
LIST_prt += [LIST_[x:y] for x in range(0, LEN) for y in range(x, LEN + 1)]
print(LIST_prt)
