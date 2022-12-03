#!/usr/bin/env python3

import sys

ROCK    = 'A'
PAPER   = 'B'
SCISSOR = 'C'
LOSE    = 'X'
DRAW    = 'Y'
WIN     = 'Z'

point_m = {LOSE: 0, DRAW: 3, WIN: 6}
point_p = {ROCK: 1, PAPER: 2, SCISSOR: 3}

answer = { LOSE: { ROCK: SCISSOR, PAPER: ROCK, SCISSOR: PAPER }, DRAW: { ROCK: ROCK, PAPER: PAPER, SCISSOR: SCISSOR }, WIN: { ROCK: PAPER, PAPER: SCISSOR, SCISSOR: ROCK } }

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines() 
    
    p = 0
    for l in lines:
        m, r = l.split(' ')
        p += point_p[answer[r][m]] + point_m[r]

    print(p)
