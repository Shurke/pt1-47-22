"""Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим
числом пробелов или символами конца строки. Определите, сколько различных
слов содержится в этом тексте."""


import string

text = input("Введите текст\n").lower()
text = text.replace("\\n", " ")
new_text = ""
for letter in text:
    if letter in string.punctuation:
        letter = " "
    new_text += letter
new_text = new_text.split()
set_1 = set(new_text)
long = len(set_1)
print(f"В вашем тексте содержится {long} уникальных слова")
