#!/usr/bin/env python3

import sys

def s2a(l):
    cur = []
    i = 0
    while i < len(l):
        if l[i] == '[':
            (r, d) = s2a(l[i+1:])
            cur.append(r)
            i += d
        elif l[i] >= '0' and l[i] <= '9':
            cur.append(int(l[i]))
        elif l[i] == ']':
            return cur, i+1

        i += 1

def add(a, b):
    return reduce([a, b])

def reduce(s, l = 0):
    print(s, l)
    if l >= 4:
        # Explode
        return (True, s[0], s[1])
    else: 
        l += 1
        for e in s:
            if isinstance(e, list):
                (fExplode, left, right) = reduce(e, l)


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    snailfish = []
    for l in lines:
        (r,d) = s2a(l[1:])
        snailfish.append(r)
        
    res = snailfish[0]
    for i in snailfish[1:]:
        res = add(res, i)