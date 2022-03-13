"""
Слова
"""
import string

str_1 = input("Введите текст").lower()
for i in string.punctuation:
    str_1 = str_1.replace(i, " ")
str_1 = set(str_1.split())
print(f"Количество слов в тексте:{len(str_1)}")
