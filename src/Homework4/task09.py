"""
Напишите функцию, выражающую заданный объем ингредиентов с использованием
минимально возможных замеров. Функция должна принимать в качестве параметра
количество единиц измерения, а также их тип (стакан, столовая или чайная ложка).
На выходе мы должны получить строку, представляющую указанное количество вещества,
с задействованием минимального количества действий и предметов. Например, если на
вход функции вы подали объем, равный 59 чайным ложкам, возвращенная строка должна быть такой:
«1 cup, 3 tablespoons, 2 teaspoons».
Подсказка:
Один стакан вмещает 16 столовых ложек, а одна столовая ложка эквивалентна трем чайным ложкам.
"""


def dispenser(unit_type, quantity):

    if unit_type == 'cup':
        result = f'{quantity} {unit_type}'
    elif unit_type == 'tablespoons':
        result = f'{quantity//16} cup, {quantity%16} tablespoons'
    elif unit_type == 'teaspoons':
        result = f'{quantity//48} cup, ' \
                 f'{quantity%48//3} tablespoons, ' \
                 f'{quantity%3} teaspoons'
    else:
        result = 'Проверьте введённые данные'

    return result


unit = input("Введите тип ёмкости (cup, tablespoons, teaspoons): ")
quan = int(input("Введите количество: "))
print(dispenser(unit, quan))
