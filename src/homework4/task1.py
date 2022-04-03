"""
Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов, не только
текущий запуск программы)
"""


import os


def write_log_of_result(func):
    """Logging wrapper

    Writes the results of function to a file res_of_functions.txt

    :param func: *args and **kwargs for func
    :return: result of func
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if not os.path.exists('res_of_functions.txt'):
            with open('res_of_functions.txt', 'w'):
                pass

        with open('res_of_functions.txt', 'a') as opened_file:
            opened_file.write(f'{result}\n')

        return result

    return wrapper


def used_func(string):
    result = string * 2
    return result


print(write_log_of_result(used_func)('Some___text'))
