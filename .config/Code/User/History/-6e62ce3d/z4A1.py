import sys

sys.setrecursionlimit(18700)

i = 0

def a():
    global i
    i += 1
    a()

try:
    a()
except RecursionError:
    print(f'recursed {i} times')

print(f'recursed {i} times')