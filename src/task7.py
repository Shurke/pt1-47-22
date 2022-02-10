import math

a = int(input())
b = int(input())
c = int(input())

if a + b > c and b + c > a and a + c > b:
    p = (a + b + c) / 2
    S = math.sqrt(p*(p - a)*(p - b)*(p - c))
    print("Площадь треугольника = " + str(S))
else:
    print("Такого треугольника не существует")