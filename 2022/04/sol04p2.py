#!/usr/bin/env python3

import re
import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    r = re.compile("(\d+)-(\d+),(\d+)-(\d+)")
    #r = re.compile("(%d+)-(%d+),(%d+)-(%d+)")
    c = 0
    for l in lines:
        print(l)
        m = r.match(l)
        (a1, a2, b1, b2) = (int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))
        if (a1 >= b1 and a2 <= b2)     \
        or (b1 >= a1 and b2 <= a2) \
        or (a1 <= b2 and a2 >= b2) \
        or (a2 >= b1 and a1 <= b1) \
        or (b1 <= a2 and b2 >= a2) \
        or (b2 >= a1 and b1 <= a1):
            c += 1

    print(c)