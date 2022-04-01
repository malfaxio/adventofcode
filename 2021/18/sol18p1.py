#!/usr/bin/env python3

import sys

def s2a(l):
    print("L: %s" % l)
    cur = []
    i = 0
    while i < len(l):
        d = 1
        if l[i] == '[':
            (r, d) = s2a(l[i+1:])
            print(r, d)
            cur.append(r)
            i += d
        elif l[i] > '0' and l[i] < '9':
            print(" n: %d" % int(l[i]))
            cur.append(int(l[i]))
        elif l[i] == ']':
            return cur, i

        i += 1


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    snailfish = []
    for l in lines:
        (r,d) = s2a(l[1:])
        snailfish.append(r)

    print(snailfish)

    
