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
        m = r.match(l)
        if (int(m.group(1)) >= int(m.group(3)) and int(m.group(2)) <= int(m.group(4))) or (int(m.group(3)) >= int(m.group(1)) and int(m.group(4)) <= int(m.group(2))):
            c += 1

    print(c)