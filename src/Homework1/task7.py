"""Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны
треугольника. Если стороны определяют треугольник, найти его площадь. Если нет,
вывести сообщение о неверных данных."""


a = int(input("Enter the length of the 1st side "))
b = int(input("Enter the length of the 2nd side "))
z = int(input("Enter the length of the 3rd side "))

if a + b > z and a + z > b and b + z > a:
    print("This is triangle")
    p = 0.5 * (a + b + z)
    s = (p * (p - a) * (p - b) * (p - z)) ** 0.5
    s = round(s, 2)
    print("area of a triangle", s)
else:
    print("Your data is not correct")
