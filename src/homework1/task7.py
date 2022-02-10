"""
7. Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь. Если нет, вывести сообщение о неверных
данных.
"""


SIDES = [float(I) for I in input('Введите размеры сторон треугольника через пробел: ').split()]
BIG_SIDE = 0
S_OF_SMALL_SIDES = 0

if len(SIDES) != 3:
    print(f'У треугольника не может быть столько сторон!')
else:

    for SIDE in SIDES:
        if SIDE > BIG_SIDE:
            BIG_SIDE = SIDE

    p = sum(SIDES) / 2
    SIDES.remove(BIG_SIDE)

    for SIDE in SIDES:
        S_OF_SMALL_SIDES += SIDE

    if S_OF_SMALL_SIDES <= BIG_SIDE:
        print('Треугольник с такими сторонами не может существовать!')
    else:
        S = (p*(p - SIDES[0])*(p - SIDES[1])*(p - BIG_SIDE))**0.5
        print(f'Площадь треугольника равна {S}.')
