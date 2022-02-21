""" Палиндром """

n = int(input("Введите число:"))
new_num = n
REVERS = 0
while n > 0:
    pro = n % 10
    REVERS = REVERS * 10 + pro
    n = n // 10
if new_num == REVERS:
    print("Это палиндром!")
else:
    print("Это не палиндром!")
