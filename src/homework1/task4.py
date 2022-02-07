"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""


string = input('Введите строку: ')
lowercase = 0
uppercase = 0
for x in string:
    if 'a' <= x <= 'z':                                         # Counting char in lower case
        lowercase += 1                                          #
    elif 'A' <= x <= 'Z':                                       # Counting char in upper case
        uppercase += 1                                          #
    # else:                                                     # To display a message about
    #     print(str(x) + ' - не является английским символом')  # an unsuitable char as a result

print('Количество английских строчных символов - ' + str(lowercase))
print('Количество английских прописных символов - ' + str(uppercase))
