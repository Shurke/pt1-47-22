num = int(input())
copy_num = num
result = 0

while num != 0:
    digit = num % 10
    result = result*10 + digit
    num = num//10
if result == copy_num:
    print("Палиндром")
else:
    print("Не палиндром")