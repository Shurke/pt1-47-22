import re

sentence = input()
no_punctuation = re.sub(r'[^\w\s]', '', sentence)
words = no_punctuation.split()
max_len = ''
for i in range(len(words)):
    if len(words[i])>len(max_len):
        max_len = words[i]

print("The word with max length is " + max_len)