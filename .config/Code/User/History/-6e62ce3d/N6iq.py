def a():
    b()
def b():
    a()

def start():
    try:
        a()
    except RecursionError:
        start()