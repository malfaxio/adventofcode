#!/usr/bin/env python3

import sys

def parseChunk(line):
    ob = { "[": "]", "(": ")", "{": "}", "<": ">" }
    cb = { "}": "{", "]": "[", ")": "(", ">": "<" }

    cf = False
    lastOpen = []
    for c in line:
        if c in "[({<":
            lastOpen.append(c)
        if c in "]})>":
            l = lastOpen.pop()
            if l != cb[c]:
                cf = True
                break

    r = ""
    if cf == False:
        while len(lastOpen) > 0:
            r += ob[lastOpen.pop()]
        
    return r

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    points = { ")": 1, "]": 2, "}": 3, ">": 4 }
    results = []
    for line in lines:
        p = 0
        for c in parseChunk(line):
            p = p*5+points[c]
        if p > 0:
            results.append(p)
    
    results.sort()
    m = int(len(results)/ 2)
    print(results[m])