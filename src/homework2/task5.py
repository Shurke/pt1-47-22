""" 5. Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


def get_list_unique(list_: list) -> list:
    """Получение списка уникальных элементов из другого списка

    :param list list_: список с элементами
    :returns: список уникальных элементов
    :rtype: list
    """
    return [x for x in list_ if list_.count(x) == 1]


TEST_CASES = [
    ([1, 2, 1], [2]),
    ([1, 2, 3, 1], [2, 3]),
    ([1, 2, 3, 1, 4], [2, 3, 4]),
    ([1, 2, 3, 1, 4, 4], [2, 3]),
    ([2, 2, 17, 17, 0], [0]),
    ([2, 2, "pew", 17, 0], ["pew", 17, 0]),
    ([], []),
    ([0, 0, 0], []),
    ([22, 17, 22, 14, 13, 11, 11, 0, 0, 7, 13], [17, 14, 7]),
]

for t in TEST_CASES:
    result = get_list_unique(t[0])
    try:
        assert result == t[1], f"FAIL: get_list_unique({t[0]}) should be {t[1]}, actual: {result}"
        print(f"OK: get_list_unique({t[0]}) == {t[1]}")
    except AssertionError as err:
        print(err)
