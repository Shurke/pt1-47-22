"""
Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно
выводить в том порядке, в котором они встречаются в списке.
"""


LIST = [ELEM for ELEM in input('Введите список через пробел: ').split()]
CHECK_LIST = []
for ITEM in LIST:
    if ITEM not in CHECK_LIST:
        print(ITEM)
        CHECK_LIST.append(ITEM)
