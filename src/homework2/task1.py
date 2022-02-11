""" 1. Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""


def fizz_buzz():
    """Выводит последовательно числа от 1 до 100 с заменой чисел на Fizz и Buzz

    Вместо чисел кратных 3 выводит Fizz,
    вместо чисел кратный 5 выводит Buzz.
    вместо чисел кратных и 3 и 5 выводит FizzBuzz
    :returns: None
    """
    for i in range(1, 101):
        result = [i]
        if not i % 3:
            result.append("Fizz")
        if not i % 5:
            result.append("Buzz")
        if len(result) > 1:
            print("".join(result[1:3]))
        else:
            print(result[0])


fizz_buzz()
