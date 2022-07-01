import gc, threading, time

i = 0

gc.set_threshold(50000)

def iteration():
    while True:
        # time.sleep(0.1)
        global i
        x = {}
        i += 1
        x[i+1] = x
        print(x)
while True:
    time.sleep(0.1)
    thread = threading.Thread(target=iteration, daemon=True)
    thread.start()
