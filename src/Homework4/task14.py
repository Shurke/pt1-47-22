"""Создайте декоратор, который вызывает задекорированную функцию пока
она не выполнится без исключений (но не более n раз - параметр
декоратора). Если превышено количество попыток, должно быть возбуждено
исключение типа TooManyErrors. Т.е. если во время работы функции
возникло какое-то исключение, то функция должна перезапуститься еще
раз. Количество перезапусков ограничено параметром декоратора."""


class TooManyErrors:
    pass


def get_type(parametr):

    """Данный декоратор вызывает функцию пока она не выполнится без
    исключений, количество попыток ограничено параметром декоратора."""

    def real_decorator(func):
        def wrapped(counter=1, *args):
            try:
                my_func = func(*args)
            except ValueError:
                if counter < parametr:
                    counter += 1
                    print("Неверные данные, попробуйте снова")
                    return wrapped(counter, *args)
                else:
                    raise TooManyErrors("Слишком много попыток")
            else:
                print("Вот результат работы вашей функции:")
                return my_func

        return wrapped

    return real_decorator


my_parametr = int(input("Введите количество попыток\n"))


@get_type(my_parametr)
def get_summ():

    """Данная функция производит сложение двух чисел"""

    num_1 = input("Введите первое число\n")
    num_2 = input("Введите второе число\n")
    summ_num = int(num_1) + int(num_2)
    return summ_num


print(get_summ())
