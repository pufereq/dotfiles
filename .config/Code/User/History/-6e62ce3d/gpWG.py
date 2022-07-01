def a():
    b()
def b():
    a()

def error():
    print('an error occured')

def start():
    try:
        a()
    except RecursionError:
        error()
start()