import random as rn, time

for i in range(10):
    rn_nrs = 0
    for i in range(1):
        rn_nrs += rn.randint(0,1)

    print(rn_nrs / 100)
    time.sleep(0.5)