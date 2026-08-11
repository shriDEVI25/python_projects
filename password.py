import random

ch="qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM!@#$%1234567890"

lenght=8
password=""

for i in range(lenght):
    password+= random.choice(ch)

print("password:",password)