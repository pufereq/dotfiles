import random

lines = open('txt/last_uni.txt').read().splitlines()
myline = random.choice(lines)
print(myline)