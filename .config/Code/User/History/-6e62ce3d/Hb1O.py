

def a():
    i += 1
    a()

try:
    i = 0
    a()
except RecursionError:
    print(f'recursed {i} times')