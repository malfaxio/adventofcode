#!/usr/bin/env python3

import sys

ROCK1    = 'A'
PAPER1   = 'B'
SCISSOR1 = 'C'
ROCK2    = 'X'
PAPER2   = 'Y'
SCISSOR2 = 'Z'

def rps(p1, p2):
    p = 0
    if (p1 == ROCK1) and (p2 == PAPER2):
        p = 6
    elif (p1 == ROCK1) and (p2 == ROCK2):
        p = 3
    elif (p1 == PAPER1) and (p2 == PAPER2):
        p = 3
    elif (p1 == PAPER1) and (p2 == SCISSOR2):
        p = 6
    elif (p1 == SCISSOR1) and (p2 == SCISSOR2):
        p = 3
    elif (p1 == SCISSOR1) and (p2 == ROCK2):
        p = 6

    return p

point = {ROCK2: 1, PAPER2: 2, SCISSOR2: 3}

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines() 
    
    p = 0
    for l in lines:
        m, r = l.split(' ')
        
        p += rps(m, r) + point[r]

    print(p)
