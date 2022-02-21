""" Палиндром """

n = int(input("Введите число:"))
new_num = n
revers = 0
while n > 0:
    pro = n % 10
    revers = revers * 10 + pro
    n = n // 10
if new_num == revers:
    print("Это палиндром!")
else:
    print("Это не палиндром!")
