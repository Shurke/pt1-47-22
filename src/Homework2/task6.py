"""Отрицательные, положительные и нули"""

positive_list = []
negative_list = []
zero_list = []
while True:
    x = (input("Введите числа, в конце введите пустое значение"))
    if x == "":
        break
    elif int(x) > 0:
        positive_list.append(x)
    elif int(x) < 0:
        negative_list.append(x)
    elif int(x) == 0:
        zero_list.append(x)
print(list(negative_list), list(zero_list), list(positive_list))
str_all = negative_list + zero_list + positive_list
for i in str_all:
    print(i)
