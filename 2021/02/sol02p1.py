#!/usr/bin/env python3

import sys
import re

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    f = open(sys.argv[1])
    lines = f.readlines()

    x = 0
    z = 0
    p = re.compile("([^\s]+)\s+(\d+)")
    for l in lines:
        m = p.match(l)
        print("C: %s" % m.group(1))
        if m.group(1) == "forward":
                x = x + int(m.group(2))
        if m.group(1) == "up":
                z = z - int(m.group(2))
        if m.group(1) == "down":
                z = z + int(m.group(2))
    
    print("X: %d  Z: %d   M: %d\n" % (x, z, z*x))
