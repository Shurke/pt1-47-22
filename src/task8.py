"""Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно
в порядке возрастания, если m<n, или в порядке убывания в противном случае."""

a = int(input(""))
b = int(input(""))
if a < b:
    for i in range(a, b + 1):
        print(i)
elif a > b:
    k = -1
    for i in range(a, b - 1, k):
        print(i)
else:
    print(a)

"""Даны два целых числа m и n (m>n). Напишите программу, которая выводит все нечетные числа
 от m до n включительно в порядке убывания."""

m = int(input(""))
n = int(input(""))
k = -2
if m % 2 == 1:
    for i in range(m, n, k):
        print(i)
elif m % 2 == 0:
    for i in range(m - 1, n, k):
        print(i)
    if m - 1 == n:
        print(n)

"""На числовой прямой даны два отрезка: (a1 - b1), (a2-b2). Напишите программу, которая находит
их пересечение."""

a1, b1 = int(input()), int(input())
a2, b2 = int(input()), int(input())
if a2 > b1 or b2 < a1:
    print('пустое множество')
elif b1 == a2:
    print(b1)
elif b2 == a1:
    print(b2)
elif a1 <= a2:
    if b1 <= b2:
        print(a2, b1)
    elif b2 < b1:
        print(a2, b2)
else:
    if b1 <= b2:
        print(a1, b1)
    elif b2 < b1:
        print(a1, b2)

"""
Given an integer,perform the following conditional actions: If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird If n is even and in the
inclusive range of 6 to 20, print Weird If n is even and greater than 20 , print - NotWeird"""

n = int(input("ВВедите число"))
if (n + 1) % 2 == 0:
    print("Weird")
elif (n + 1) % 2 == 1 and n > 2 and n <= 5:
    print("Not Weird")
elif (n + 1) % 2 == 1 and n >= 6 and n <= 20:
    print("Weird")
elif (n + 1) % 2 == 1 and n >= 20:
    print("Not Weird")
