#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    f = open(sys.argv[1])
    lines = f.readlines()
    c = 0
    for line in lines:
        t = line.strip().split(" | ")
        signals = t[0].split(" ")
        outputs = t[1].split(" ")
        for o in outputs:
            if len(o) in [2, 4, 3, 7]:
                c += 1
        print(signals, outputs)
    
    print("N. of unique digits: %d" % c)