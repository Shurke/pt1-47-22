"""
5. Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
"""


a = 0
b = 1
n = input('Введите число: ')
n = int(n)
i = 0
while i < n - 2:
    fib_sum = a + b
    a = b
    b = fib_sum
    i = i + 1
print(b)
# a - first number
# b - second number
