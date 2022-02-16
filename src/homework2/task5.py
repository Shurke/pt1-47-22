"""
Дан список. Выведите те его элементы, которые встречаются в списке
только один раз. Элементы нужно выводить в том порядке, в котором
они встречаются в списке.
Первый вариант решения:
list1 = [int(elem) for elem in input("Ведите список через пробел: ").split()]
list2 = []
for item1 in range(len(list1)):
    if list1[item1] not in list2:
        list2.append(list1[item1])
        print(list1[item1], end=' ')
Второй вариант решения:
"""

list1 = [int(elem) for elem in input("Ведите список через пробел: ").split()]
for item1 in range(len(list1)):
    for item2 in range(len(list1)):
        if item1 != item2 and list1[item1] == list1[item2]:
            break
    else:
        print(list1[item1], end=' ')
