#!/usr/bin/env python3

import sys

def s2a(s):
    r = []
    i = 0
    while i < range(len(s)):
        print(s[i])
        if s[i] == "[":
            i += 1
            (n,r) = s2a(s[i+1:])
        elif s[i] == "]":
            return r
        elif s[i] != "," and 0 <= int(s[i]) <= 9:
            r.append(int(s[i]))


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    snailfish = []
    for l in lines:
        snailfish.append(s2a(l))

    print(snailfish)

    
