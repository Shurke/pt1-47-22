"""
Используя определение подсписка из задачи №8, напишите программу, возвращающую список, содержащий все возможные подсписки заданного.
Например, в число подсписков списка [1, 2, 3] входят следую-щие: [], [1], [2], [3], [1, 2], [2, 3] и [1, 2, 3].
Заметьте, что ваша программа должна вернуть как минимум один пустой список, гарантированно являющийся подсписком для любого списка.
"""

print("Введите список элементов через пробел")
main_list = [i for i in input().split()]
sublists = [[]]
for i in range(len(main_list) + 1):
    for j in range(i):
        sublists.append(main_list[j:i])
print(sublists)

