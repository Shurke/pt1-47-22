"""
Во многих кулинарных книгах до сих пор можно встретить рецепты, в которых ингредиенты отмеряются
стаканами, чайными и столовыми ложками. И хотя при наличии этих нехитрых предметов таким рецептам
следовать довольно удобно, бывает трудно быстро преобразовать подобные меры при приготовлении
рождественского ужина на огромную семью. Например, если в рецепте сказано взять четыре столовые
ложки того или иного ингредиента, то при увеличении выхода в четыре раза можно просто отсчитать 16
столовых ложек. Однако гораздо проще было бы привести эту меру к одному стакану.
Напишите функцию, выражающую заданный объем ингредиентов с использованием минимально возможных
замеров. Функция должна принимать в качестве параметра количество единиц измерения, а также их тип
(стакан, столовая или чайная ложка). На выходе мы должны получить строку, представляющую указанное
количество вещества, с задействованием минимального количества действий и предметов. Например, если
на вход функции вы подали объем, равный 59 чайным ложкам, возвращенная строка должна быть такой: «1
cup, 3 tablespoons, 2 teaspoons».
Подсказка. Один стакан вмещает 16 столовых ложек, а одна столовая ложка эквивалентна трем чайным
ложкам.
"""


def cooking(numb, name) -> str:
    """Accepts name in (cups, tablespoons, teaspoons) and amount of them.

    Return string with numbers of cups, tablespoons and teaspoons.
    """
    table_in_cup = 16
    tea_in_table = 3
    tea_in_cup = tea_in_table * table_in_cup

    if name == 'teaspoons':
        general_tea = numb
    elif name == 'tablespoons':
        general_tea = numb * tea_in_table
    elif name == 'cups':
        general_tea = numb * tea_in_cup
    else:
        return 'Some trouble with type of container. Is it correct?'

    num_of_cup = general_tea // tea_in_cup
    num_of_table = (general_tea - num_of_cup * tea_in_cup) // tea_in_table
    num_of_tea = general_tea - num_of_cup * tea_in_cup - num_of_table * tea_in_table
    return f'Necessary {num_of_cup} cup, {num_of_table} tablespoons, {num_of_tea} teaspoons'


def main():
    """Main function"""
    while True:
        input_str = input('Please enter data for conversion (example - 59 teaspoons): ')
        input_list = input_str.split()
        if len(input_list) == 2:
            container = input_list[1]
            number = input_list[0]
            if container in ('cup', 'tablespoons', 'teaspoons') and number.isdigit():
                ans = cooking(numb=number, name=container)
            else:
                ans = 'Some mistake in input data'
        else:
            ans = 'Use example: 59 teaspoons'
        print(ans)


if __name__ == "__main__":
    main()
