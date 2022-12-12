#!/usr/bin/env python3

import re
import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    p = re.compile("addx\s+(\-?[\d]+)")
    cycle = 0
    x = 1
    power = 0
    for l in lines:
        if l[0:4] == "noop":
            cycle += 1
            if (cycle == 20) or (cycle > 20 and (cycle - 20) % 40 == 0):
                power += cycle * x
                print("Cycle: %d   X: %d  Power: %d" % (cycle, x, cycle * x))
        elif l[0:4] == 'addx':
            cycle += 1
            if (cycle == 20) or (cycle > 20 and (cycle - 20) % 40 == 0):
                power += cycle * x
                print("Cycle: %d   X: %d  Power: %d" % (cycle, x, cycle * x))
            cycle += 1
            if (cycle == 20) or (cycle > 20 and (cycle - 20) % 40 == 0):
                power += cycle * x
                print("Cycle: %d   X: %d  Power: %d" % (cycle, x, cycle * x))
            x += int(p.search(l)[1])

    print(power)