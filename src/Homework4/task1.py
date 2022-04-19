""""Создайте декоратор, который хранит результаты вызовов
функции (за все время вызовов, не только текущий запуск программы)"""


def write_in_file(func):

    """Данный декоратор записывает данные вызова функции за
    все время вызовов."""

    def wrapper(*args, **qwargs):
        file = open('my_sum.txt', 'a')
        result = func(*args, **qwargs)
        file.write(f"{result}" + " ")
        file.close()
        file = open('my_sum.txt')
        print(f"вот данные которые храняться сейчас в "
              f"файле \n{file.read()}")
        file.close()
        return result
    return wrapper


@write_in_file
def sum_of_number(digit_1, digit_2):

    """Данная функция производит сложение двух чисел"""

    summ = digit_1 + digit_2
    return summ


num_1 = int(input("Введите первое число\n"))
num_2 = int(input("Введите второе число\n"))

my_func = sum_of_number(num_1, num_2)
