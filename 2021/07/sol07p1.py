#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    positions = [int(x) for x in open(sys.argv[1]).read().strip().split(',')]

    fuel = max(positions)*len(positions)
    minp = 0
    for p in range(min(positions),max(positions)+1):
        f = sum([abs(x-p) for x in positions])
        print((p,f))
        if f < fuel:
            minp = p
            fuel = f

    print("Min fuel: %d @ %d" % (fuel, minp))