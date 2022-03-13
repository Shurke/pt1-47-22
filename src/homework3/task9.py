"""
Дом N
"""
newspapers_set = []
for i in range(1, 76):
    newspapers_set.append(i)
magazine_set = []
for x in range(1, 28):
    magazine_set.append(x)
combo_set = []
for y in range(1, 14):
    combo_set.append(y)
dif_newspapers_set = set(newspapers_set).difference(combo_set)
dif_magazine_set = set(magazine_set).difference(combo_set)
n = len(dif_magazine_set) + len(dif_newspapers_set)
print("Количество семей, проживающих в дому N: ", n)
