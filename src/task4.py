import re

sentence = input()
regex = "^[a-zA-Z]+$"  # regex for latin characters only
pattern = re.compile(regex)  # compiling regex expression
capital_letters = 0
small_letters = 0

for i in range(len(sentence)):
    if(pattern.search(sentence[i]) is not None):
        if(sentence[i].islower()==True):
            small_letters += 1
        elif(sentence[i].isupper()==True):
            capital_letters += 1

print("Capital letters " + str(capital_letters))
print("Small letters " + str(small_letters))