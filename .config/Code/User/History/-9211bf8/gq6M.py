import random

lines = open('last_uni.txt').read().splitlines()
myline = random.choice(lines)
print(myline)