"""
Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов, не только
текущий запуск программы)
"""


def get_list_of_result(func):
    """Logging wrapper"""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        import os

        if os.path.exists('res_of_functions.txt') is False:
            with open('res_of_functions.txt', 'w'):
                pass

        with open('res_of_functions.txt', 'a') as opened_file:
            opened_file.write(f'{result}\n')

        return result

    return wrapper


def used_func(string):

    result = string * 2

    return result


print(get_list_of_result(used_func)('Some___text'))
