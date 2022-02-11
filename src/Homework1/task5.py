"""Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится"""

num1 = 0
num2 = 1
n = input("Enter the sequence number of Fibonacci (n) = ")
n = int(n)
i = 0
if n > 0:
    while i < n - 2:
        num_sum = num1 + num2
        num1 = num2
        num2 = num_sum
        i = i + 1
    print("For n =", n, "Fn = ", num2)
elif n < 0:
    while i > n + 2:
        num_sum = num1 - num2
        num1 = num2
        num2 = num_sum
        i = i - 1
    print("For n =", n, "Fn = ", num2)
else:
    while i < n + 2:
        num_sum = num1 + num2
        num1 = - num2
        num2 = num_sum
        i = i + 1
    print("For n =", n, "Fn = ", num2)
