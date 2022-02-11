""" 3. Tuple practice
Создайте кортеж из одного элемента,
чтобы при итерировании по этому элементу последовательно выводились значения 1, 2, 3.
Убедитесь что len() исходного кортежа возвращает 1.
"""


def solution():
    """Реализация решения

    :returns: None
    """
    my_tuple = ([1, 2, 3],)
    for tuple_elem in my_tuple:
        for value in tuple_elem:
            print(value)
    print(f"tuple length: {len(my_tuple)}")


solution()
