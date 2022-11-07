#!/usr/bin/env python3

import random
import re
import sys

position = [0,0]
times = -1

def dice():
    global times  

    times += 1

    return (times % 100) + 1
    #return random.randint(1,100)

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    lines = open(sys.argv[1]).read().splitlines()

    for l in lines:
        m = re.search("Player (\d+) starting position: (\d+)", l)
        position[int(m.group(1))-1] = int(m.group(2))-1

    print(position)
    score = [0,0]
    turn = 0
    for turn in range(160):
    #while score[0] < 1000 and score[1] < 1000:
        turn += 1
        print("Turn: %d" % (turn))
        for p in range(2):
            pt = 0
            print("Player %d rolls:" % p, end="")
            for i in range(3):
                x = dice()
                print(" %d" % x, end="")
                pt += x
            
            position[p] = (position[p] + pt) % 10
            if position[p] == 0:
                score[p] += 10
            else:
                score[p] += position[p]+1

            print(" move to space %d for a total score of %d" % ( position[p]+1, score[p]))

            if score[p] >= 1000:
                break

        if score[p] >= 1000:
            print("Times %d" % times)
            break
        
