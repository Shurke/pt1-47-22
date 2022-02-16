"""Используя определение подсписка из задачи №8, напишите программу,
возвращающую список, содержащий все возможные подсписки заданного.
Например, в число подсписков списка [1, 2, 3] входят
следую-щие: [], [1], [2], [3], [1, 2],[2, 3] и [1, 2, 3].
Заметьте, что ваша программа должна вернуть как минимум один пустой
список, гарантированно являющийся подсписком для любого списка."""

lis1 = input("Введите список через пробел\n")
lis1 = lis1.split()
new_lis = []
start = 0
end = 0
long = len(lis1)
while start < len(lis1):
    end += 1
    if lis1[start:end] not in new_lis:
        new_lis.append(lis1[start:end])
        if end == len(lis1):
            end = 0
            start += 1
print("В ваш список входят следующие подсписки:\n", new_lis)
