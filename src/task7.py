"""Даны: три стороны треугольника. Требуется: проверить,
действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
 Если нет, вывести сообщение о неверных данных.
"""

A = 5
B = 4
C = 3

if A + B > C and A + C > B and B + C > A:
    D = (C + B + C) / 2
    S = (D * (D - A) * (D - B) * (D - C)) ** 0.5
    print(S)
else:
    print("Не треугольник")
