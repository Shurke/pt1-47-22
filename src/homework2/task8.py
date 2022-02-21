""" 8. Содержит ли список подмножество элементов?
Подмножеством элементов, или подсписком (sublist), мы будем называть список,
являющийся составной частью большего списка.
Подсписок может содержать один элемент, множество элементов, а также быть пустым.
Например, [1], [2], [3] и [4] являются подсписками списка [1, 2, 3, 4].
Список [2, 3] также входит в состав [1, 2, 3, 4], но при этом список [2, 4] не является подсписком
[1, 2, 3, 4], поскольку в исходном списке числа 2 и 4 не соседствуют друг с другом.
Пустой список может быть рассмотрен как подсписок для любого списка.
Таким образом, список [] является под- списком [1, 2, 3, 4].
Также список является подсписком самого себя, то есть [1, 2, 3, 4] – это подсписок для [1, 2, 3, 4].
В рамках данного упражнения вам необходимо написать программу, определяющую, является ли один список
подсписком другого. На вход должны поступать два списка – larger и smaller.
Программа должна возвращать значение True только в том случае, если список smaller является
подсписком списка larger.
"""


def is_sublist(larger, smaller: list) -> bool:
    """Возвращает результат проверки входимости подсписка в список

    :param list larger: список в котором осуществляется проверка
    :param list smaller: подсписок который необходимо проверить на входимость
    :returns: результат проверки
    :rtype: bool
    """
    larger_len, smaller_len = len(larger), len(smaller)
    if smaller_len > larger_len:
        return False
    if smaller == larger or smaller == []:
        return True
    for i in range(0, larger_len):
        if smaller == larger[i:i + smaller_len]:
            return True
    return False


TEST_CASES = [
    (([1, 2, 1], [1, 2]), True),
    (([1, 2, 1], [2, 1]), True),
    (([1, 2, 1], [1]), True),
    (([1, 2, 1], []), True),
    (([1, 2, 1], [1, 3]), False),
    (([1, 2, 1], [1, 2, 1]), True),
    (([1, 2, 1], [1, 2, 1, 3]), False),
    (([1, 2, 3, 1, 17, 500, 314, 22, 97, 13], [1, 2]), True),
    (([1, 2, 3, 1, 17, 500, 314, 22, 97, 13], [2, 3, 1, 17, 500, 314, 22, 97, 13]), True),
    (([1, 2, 3, 1, 17, 500, 314, 22, 97, 13], [500, 314]), True),
    (([1, 2, 3, 1, 17, 500, 314, 22, 97, 13], [2, 17, 1, 44]), False),
]

for t in TEST_CASES:
    result = is_sublist(t[0][0], t[0][1])
    try:
        assert result == t[1], (
            f"FAIL: is_sublist({t[0][0]}, {t[0][1]}) should be {t[1]}, actual: {result}")
        print(f"OK: is_sublist({t[0][0]}, {t[0][1]}) == {t[1]}")
    except AssertionError as err:
        print(err)
