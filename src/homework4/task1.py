"""
Создайте декоратор, который хранит результаты вызовов функции (за все время
вызовов, не только текущий запуск программы)
"""
from functools import wraps


def decor_record(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = (func(*args, **kwargs))
        with open('result_func.txt', 'a+', encoding='utf-8') as file:
            file.write(f'{result}\n')
        return result
    return wrapper


@decor_record
def get_counter(a, b):
    """Складывает два числа"""

    add = a + b
    return add


number_1, number_2 = input("Введите два числа через пробел: ").split()
print(get_counter(int(number_1), int(number_2)))
