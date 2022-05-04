"""Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов, не только
 текущий запуск программы)
"""


def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('function_results.txt', 'a') as file:
            file.write(f'{result}\n')
        return result
    return wrapper


@decorator
def one(a, b):
    i = [x for x in range(a ** b) if x % 2 == 0]
    return i


print(one(10, 4))
