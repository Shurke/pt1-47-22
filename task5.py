"""
Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""

list = [int(a) for a in input("Введите числа через пробел: ").split()]
for i in range(len(list)):
    for j in range(len(list)):
        if i != j and list[i] == list[j]:
            break
    else:
        print(list[i], end=' ')