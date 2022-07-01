import random as rn, time

for i in range(10):
    rn_nrs = 0
    for i in range(1000):
        rn_nrs += rn.randint(0,100)

    print(rn_nrs / 1000)
    time.sleep(0.5)