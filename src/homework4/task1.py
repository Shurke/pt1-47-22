"""
Создайте декоратор, который хранит результаты вызовов функции (за все время
вызовов, не только текущий запуск программы)
"""


def decor_record(func):
    def wrapper(*args, **kwargs):
        result = (func(*args, **kwargs))
        with open('result_func.txt', 'a', encoding='utf-8') as file:
            file.write(f'{result}\n')
        with open('result_func.txt', 'r', encoding='utf-8') as file:
            output_file = file.readlines()
            file = [x.strip() for x in output_file]
            print(f"Все результаты вызовов функции: {file}")
        return result
    return wrapper


@decor_record
def get_counter(param):
    add = param + param
    return add


print(get_counter("hbgf"))
