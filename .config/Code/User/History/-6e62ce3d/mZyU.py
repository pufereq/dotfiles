import gc, threading

i = 0

gc.set_threshold(50000)

def iteration():
    while True:
        global i
        x = {}
        i += 1
        x[i+1] = x
        print(x)
while True:
    thread = threading.Thread(target=iteration, daemon=True)
    thread.start()
