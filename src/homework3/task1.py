""" 1. Dict comprehensions
Создайте словарь с помощью генератора словарей,
так чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел.
"""


def dict_generator():
    """Создает словарь с ключами 1..20 и значениями равными ключ**3

    :returns: словарь с результатом
    :rtype: dict
    """

    return {key: key**3 for key in range(1, 21)}


print(dict_generator())
