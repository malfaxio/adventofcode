#!/usr/bin/env python3

import re
import sys

display = []


def turnOn(cycle, x):
    global display

    p = cycle % 40
    r = int(cycle / 40)
    if (x - 1) <= p <= (x + 1):
        display[r][p] = 1

def draw():
    for r in display:
        for c in r:
            if c == 1:
                print('#', end='')
            else:
                print('.', end='')
        print()

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    # Init display
    for y in range(6):
        d = []
        for x in range(40):
            d.append(0)
        display.append(d)

    p = re.compile("addx\s+(\-?[\d]+)")
    cycle = 0
    x = 1
    for l in lines:
        if l[0:4] == "noop":
            turnOn(cycle, x)            
            cycle += 1
        elif l[0:4] == 'addx':
            turnOn(cycle, x)
            cycle += 1
            turnOn(cycle, x)
            cycle += 1
            x += int(p.search(l)[1])
        draw()
        print()
