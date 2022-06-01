"""
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""


def counter(func):
    counters = {}

    def wrapper(*args, **kwargs):
        counters[func] = counters.get(func, 0) + 1
        if counters[func] == number_of_calls:
            print(f'Функция {func.__name__} вызвана {counters[func]} раз')

        result = func(*args, **kwargs)

        return result

    return wrapper


@counter
def any_funk():
    pass


number_of_calls = int(input('Введите количество вызовов функции: '))

for i in range(number_of_calls):
    any_funk()
