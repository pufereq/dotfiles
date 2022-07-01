import random as rn, time

rn_nrs = 0
for i in range(10):
    for i in range(100):
        rn_nrs += rn.randint(0,100)

    print(rn_nrs / 100)
    time.sleep(0.5)