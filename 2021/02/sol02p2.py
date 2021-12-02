#!/usr/bin/env python3

import sys
import re

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    f = open(sys.argv[1])
    lines = f.readlines()

    x = 0
    z = 0
    aim = 0
    p = re.compile("([^\s]+)\s+(\d+)")
    for l in lines:
        m = p.match(l)
        cmd = m.group(1)
        v = int(m.group(2))
        print("C: %s  V: %d" % (cmd, v))
        if m.group(1) == "forward":
                x = x + v
                z = z + aim*v
        if m.group(1) == "up":
                aim = aim - v
        if m.group(1) == "down":
                aim = aim + v
    
    print("X: %d  Z: %d AIM: %d  M: %d\n" % (x, z, aim, z*x))
