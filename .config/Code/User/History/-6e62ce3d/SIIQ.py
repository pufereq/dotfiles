import gc, threading

i = 0

gc.set_threshold(50000)

def iteration():
    global i
    x = {}
    i += 1
    x[i+1] = x
    print(x)

thread = threading.Thread(target=iteration, daemon=True)
thread.start()
