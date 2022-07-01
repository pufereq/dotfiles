import random

lines = open('file.txt', 'r').splitlines()
myline = random.choice(lines)
print(myline)