import sys

sys.setrecursionlimit(10)

i = 0

def a():
    global i
    i += 1
    a()

try:
    a()
except RecursionError:
    print(f'recursed {i} times')