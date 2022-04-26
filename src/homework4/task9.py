"""Во многих кулинарных книгах до сих пор можно встретить рецепты, в которых ингредиенты отмеряются
стаканами, чайными и столовыми ложками. И хотя при наличии этих нехитрых предметов таким рецептам
следовать довольно удобно, бывает трудно быстро преобразовать подобные меры при приготовлении
рождественского ужина на огромную семью. Например, если в рецепте сказано взять четыре столовые
ложки того или иного ингредиента, то при увеличении выхода в четыре раза можно просто отсчитать
16 столовых ложек. Однако гораздо проще было бы привести эту меру к одному стакану.
Напишите функцию, выражающую заданный объем ингредиентов с использованием минимально возможных
замеров. Функция должна принимать в качестве параметра количество единиц измерения, а также их тип
(стакан, столовая или чайная ложка). На выходе мы должны получить строку, представляющую указанное
количество вещества, с задействованием минимального количества действий и предметов. Например, если
на вход функции вы подали объем, равный 59 чайным ложкам, возвращенная строка должна
быть такой: «1 cup, 3 tablespoons, 2 teaspoons». Подсказка. Один стакан вмещает 16 столовых ложек,
а одна столовая ложка эквивалентна трем чайным ложкам."""


def kitchen(numb, tool):
    """A function that counts the use of the minimum possible tools
    :param numb: numb of ingredients
    :param tool: tools
    :return: line with a minimum numb of actions and items"""
    if tool == 'cup':
        return f'{numb} {tool}'
    elif tool == 'tablespoons':
        cup = numb // 16
        tablespoon = numb % 16
        return f'{cup} cup, {tablespoon} tablespoon'
    elif tool == 'teaspoons':
        cup = numb // 48
        tablespoon = (numb % 48) // 3
        teaspoon = numb % 3
        return f'{cup} cup, {tablespoon} tablespoons, {teaspoon} teaspoons'
    return numb, tool


quant_ingredients, cook_type = (input('Enter the amount of ingredients '
                                      'and type of tool for cooking '
                                      '(cup, tablespoons or teaspoons): ')).split()
print(kitchen(int(quant_ingredients), cook_type))
