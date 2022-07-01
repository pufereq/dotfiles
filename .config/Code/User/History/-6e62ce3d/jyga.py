
i = 0

def a():
    i += 1
    a()

try:
    a()
except RecursionError:
    print(f'recursed {i} times')