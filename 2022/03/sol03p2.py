#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    p = 0
    for i in range(len(lines)):
        if ((i+1) % 3) == 0:
            for c in lines[i]:
                if c in lines[i-1] and c in lines[i-2]:
                    break
                
            if 'a' <= c <= 'z':
                p += ord(c)-96
            elif 'A' <= c <= 'Z':
                p += ord(c)-38

    print(p)
