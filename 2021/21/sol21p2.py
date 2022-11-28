#!/usr/bin/env python3

import random
import re
import sys

position = [0,0]
score = [0, 0]
times = 0

def dice():
    global times  

    times += 1
    r = (times % 100)
    if r == 0:
        r = 100

    return r

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    lines = open(sys.argv[1]).read().splitlines()

    for l in lines:
        m = re.search("Player (\d+) starting position: (\d+)", l)
        position[int(m.group(1))-1] = int(m.group(2))

    print(position)

    while (score[0] < 1000) and (score[1] <1000):
        # player 1
        l = dice() + dice() + dice()
        position[0] = (position[0] + l) % 10
        if position[0] == 0:
            position[0] = 10
        score[0] += position[0]
        if score[0] >= 1000:
            break

        # player 2
        l = dice() + dice() + dice()
        position[1] = (position[1] + l) % 10
        if position[1] == 0:
            position[1] = 10
        score[1] += position[1]
        if score[0] >= 1000:
            break

    if score[0] >= 1000:
        wi = score[0]
        lo = score[1]
    else:
        wi = score[1]
        lo = score[0]
    res = lo * times
    print("Winner: %d  Loser: %d  Times: %d  Result: %d" % (wi, lo, times, res))
