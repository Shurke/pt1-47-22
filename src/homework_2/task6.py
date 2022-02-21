"""Отрицательные, положительные и нули"""

a = []
b = []
c = []
while True:
    x = (input("Введите числа, в конце введите пустое значение"))
    if x == "":
        break
    elif int(x) > 0:
        a.append(x)
    elif int(x) < 0:
        b.append(x)
    elif int(x) == 0:
        c.append(x)
print(list(b), list(c), list(a))
str_all = b + c + a
for i in str_all:
    print(i)
