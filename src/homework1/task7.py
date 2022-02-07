"""
7. Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника. Если стороны
определяют треугольник, найти его площадь. Если нет, вывести сообщение о неверных данных.
"""


sides = [int(i) for i in input('Введите размеры сторон треугольника через пробел: ').split()]
big_side = 0
s_of_small_sides = 0

if len(sides) != 3:
    print(f'У треугольника не может быть столько сторон!')
else:

    for side in sides:
        if side > big_side:
            big_side = side

    p = sum(sides) / 2
    sides.remove(big_side)

    for side in sides:
        s_of_small_sides += side

    if s_of_small_sides <= big_side:
        print('Треугольник с такими сторонами не может существовать!')
    else:
        side_1 = sides[0]
        side_2 = sides[1]
        side_3 = big_side
        S = (p*(p - side_1)*(p - side_2)*(p - side_3))**0.5
        print(f'Площадь треугольника равна {S}.')
