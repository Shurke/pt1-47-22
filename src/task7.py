"""Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
 Если нет, вывести сообщение о неверных данных.
"""

dlin = 5
vis = 4
shir = 3

if dlin + vis > shir and dlin + shir > vis and vis + shir > dlin:
    midl = (dlin + vis + shir) / 2
    s = (midl * (midl - dlin) * (midl - vis) * (midl - shir)) ** 0.5
    print(s)
else:
    print("Не треугольник")

