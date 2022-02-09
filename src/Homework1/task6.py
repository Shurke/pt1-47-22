""" Определите, является ли число палиндромом (читается слева направо и справа
налево одинаково).
 Число положительное целое, произвольной длины. Задача требует работать только с
 числами (без конвертации числа в строку или что-нибудь еще) """


num = int(input("Enter number "))
num_1 = num
new_num = 0
while num != 0:
    num2 = num % 10
    new_num = new_num * 10 + num2
    num = int(num / 10)

if new_num == num_1:
    print("This number is palindrome")
else:
    print("This number is not a Palindrome")
