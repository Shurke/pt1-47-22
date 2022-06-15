"""
Во многих кулинарных книгах до сих пор можно встретить рецепты, в которых
ингредиенты отмеряются стаканами, чайными и столовыми ложками. И хотя при
наличии этих нехитрых предметов таким рецептам следовать довольно удобно, бывает
трудно быстро преобразовать подобные меры при приготовлении рождественского
ужина на огромную семью. Например, если в рецепте сказано взять четыре столовые
ложки того или иного ингредиента, то при увеличении выхода в четыре раза можно
просто отсчитать 16 столовых ложек. Однако гораздо проще было бы привести эту
меру к одному стакану.
Напишите функцию, выражающую заданный объем ингредиентов с использованием
минимально возможных замеров. Функция должна принимать в качестве параметра
количество единиц измерения, а также их тип (стакан, столовая или чайная ложка).
На выходе мы должны получить строку, представляющую указанное количество
вещества, с задействованием минимального количества действий и предметов.
Например, если на вход функции вы подали объем, равный 59 чайным ложкам,
возвращенная строка должна быть такой: «1 cup, 3 tablespoons, 2 teaspoons».
Подсказка. Один стакан вмещает 16 столовых ложек, а одна столовая ложка
эквивалентна трем чайным ложкам.
"""


def unit_conversion(number, name):
    """Converts a given amount of ingredients to the smallest possible measurements

    :param number: Number of units
    :param name: Тип: glass, tablespoon or teaspoon
    :return: A string representing the specified amount of the substance, with
    involving a minimum number of actions and items

    """
    if name not in ("cups", "tablespoons", "teaspoons"):
        return "The entered type is invalid"
    if number <= 0:
        return "The amount entered must be greater than zero"
    if name == "cups":
        return f"{number} {name}"
    elif name == "tablespoons":
        cup = number // 16
        tablespoon = number % 16
        return f"{cup} cups, {tablespoon} tablespoons"
    elif name == "teaspoons":
        cup = number // 48
        tablespoon = (number % 48) // 3
        teaspoon = number % 3
        return f"{cup} cups, {tablespoon} tablespoons, {teaspoon} teaspoons"


if __name__ == "__main__":
    str_input = input("Enter the amount of ingredients, for example, 59 tablespoons: ").split()
    number_input = int(str_input[0])
    type_input = str_input[1]
    print(unit_conversion(number_input, type_input))
