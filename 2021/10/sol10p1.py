#!/usr/bin/env python3

import sys

def parseChunk(line):
    cb = { "}": "{", "]": "[", ")": "(", ">": "<" }
    r = ""
    lastOpen = []
    for c in line:
        if c in "[({<":
            lastOpen.append(c)
        if c in "]})>":
            l = lastOpen.pop()
            if l != cb[c]:
                r = c
                break
        
    return r

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    corrupted = []
    points = { "}": 1197, "]": 57, ")": 3, ">": 25137 }
    for line in lines:
        corruptchar = parseChunk(line)
        if len(corruptchar) > 0:
            corrupted.append(points[corruptchar])
    
    print(sum(corrupted))