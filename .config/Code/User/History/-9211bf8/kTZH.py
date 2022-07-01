import random

lines = open('last_uni.txt', 'r').splitlines()
myline = random.choice(lines)
print(myline)