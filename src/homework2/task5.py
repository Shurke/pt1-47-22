""" 5. Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


def get_list_unique(lst):
    """Получение списка уникальных элементов из другого списка

    :param list lst: список с элементами
    :returns: список уникальных элементов
    :rtype: list
    """
    return [x for x in lst if lst.count(x) == 1]


TEST_CASES = [
    [1, 2, 1],
    [1, 2, 3, 1],
    [1, 2, 3, 1, 4],
    [1, 2, 3, 1, 4, 4],
    [2, 2, 17, 17, 0],
    [2, 2, "pew", 17, 0],
    [],
    [0, 0, 0],
    [22, 17, 22, 14, 13, 11, 11, 0, 0, 7, 13],
]
for t in TEST_CASES:
    print(f"Уникальные элементы списка {t} = {get_list_unique(t)}")
