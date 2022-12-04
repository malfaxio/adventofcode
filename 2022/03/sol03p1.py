#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    p = 0
    for l in lines:
        for c in l[0:int(len(l)/2)]:
            if c in l[int(len(l)/2):]:
                break
        if 'a' <= c <= 'z':
            p += ord(c)-96
        elif 'A' <= c <= 'Z':
            p += ord(c)-38

    print(p)
