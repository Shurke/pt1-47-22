""" 4. Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def count_pairs(list_: list) -> int:
    """Подсчет количества пар элементов в списке чисел

    :param list list_: список чисел
    :returns: количество пар
    :rtype: int
    """
    counter = 0
    lst_len = len(list_)
    for i in range(lst_len - 1):
        counter += list_[i + 1: lst_len].count(list_[i])
    return counter


TEST_CASES = [
    ([1, 1, 1], 3),
    ([1, 1, 1, 1], 6),
    ([1, 1, 1, 1, 1], 10),
    ([1, 1, 1, 1, 1, 1], 15),
    ([2, 2, 17, 17, 0], 2),
]

for t in TEST_CASES:
    result = count_pairs(t[0])
    try:
        assert result == t[1], f"FAIL: count_pairs({t[0]}) should be {t[1]}, actual: {result}"
        print(f"OK: count_pairs({t}) == {t[1]}")
    except AssertionError as err:
        print(err)
