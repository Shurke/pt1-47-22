#  4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке. Учитывать только
#  английские буквы.


text = input('Введите текст: ')
s = 0
B = 0

for i in text:
    if 'a' <= i <= 'z':
        s += 1
    else:
        if 'A' <= i <= 'Z':
            B += 1

print(s)
print(B)
