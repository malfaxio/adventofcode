#!/usr/bin/env python3

import sys

def cost(p):
    c = 0
    for i in range(p):
        c += (i+1)
    return c

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    positions = [int(x) for x in open(sys.argv[1]).read().strip().split(',')]

    minp = 0
    for p in range(min(positions),max(positions)+1):
        f = sum([cost(abs(x-p)) for x in positions])
        try:
            if f < fuel:
                minp = p
                fuel = f
        except NameError:
            fuel = f

    print("Min fuel: %d @ %d" % (fuel, minp))