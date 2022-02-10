a = input()
b = ''

for i in range(len(a)):
    if a[i] == ' ' or a[i] in b:
        continue
    else:
        b = b + a[i]

print(b)