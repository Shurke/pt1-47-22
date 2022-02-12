"""Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.
"""
a = int(input())
b = int(input())
c = int(input())
if a + b > c or a + c > b or b + c > a:
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
else:
    print("Фигура не является треугольником, либо введены неверные данные")
