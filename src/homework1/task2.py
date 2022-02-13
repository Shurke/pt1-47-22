"""
Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
"""

from string import punctuation

sentence = input('Введите предложение ')

for i in punctuation:                                 # iterate over sentence char over
    sentence = sentence.replace(i, " ")               # a list of punctuation characters

sentence_clr = sentence.split()                       # divide the sentence by spaces
L = 0                                                 # variable number of characters in a word
for c in sentence_clr:                                # loop through the words in the cleared list
    d = len(c)                                        # variable number of characters in a word
    if d > L:
        L = d
        wrd = c
print(f'Самое длинное слово в предложении - "{wrd}"')
