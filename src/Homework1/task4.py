""" Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы."""

import string
message = input("enter your message ")
message_low = 0
message_high = 0
high = "QWERTYUIOPASDFGHJKLZXCVBNM"
low = "qwertyuiopasdfghjklzxcvbnm"
for letter in message:
    if letter in string.ascii_uppercase:
        message_high += 1
    elif letter in string.ascii_lowercase:
        message_low += 1
print("Your massage: ", message)
print(message_low, "lowercase letters in your massage")
print(message_high, "capital letter in your massage")
