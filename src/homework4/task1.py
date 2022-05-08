"""
Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов, не только
текущий запуск программы)
"""


def result_dec(func):
    """save the function call to file

    :param func: arguments for func
    :return: results to file
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('function_result.txt', 'a') as file:
            file.write(f'{result}\n')
        return result

    return wrapper


@result_dec
def user_func(something):
    test = something + ' ' + something

    return test


if __name__ == '__main__':
    print(user_func('hello!'))
