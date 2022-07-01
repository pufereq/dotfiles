def a():
    b()
def b():
    a()

try:
    a()
except RecursionError:
    pass