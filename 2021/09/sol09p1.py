#!/usr/bin/env python3

import sys

def checkMinimum(d, x, y):
    p = int(d[y][x])
    mx = len(d[y])-1
    my = len(d)-1
    
    if y > 0 and int(d[y-1][x]) <= p:
        return False
    if y < my and int(d[y+1][x]) <= p:
        return False
    if x > 0 and int(d[y][x-1]) <= p:
        return False
    if x < mx and int(d[y][x+1]) <= p:
        return False

    return True

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    deeps = open(sys.argv[1]).read().splitlines()

    risklevel = []
    for y in range(len(deeps)):
        for x in range(len(deeps[y])):
            if checkMinimum(deeps, x, y):
                risklevel.append(int(deeps[y][x])+1)


    print("Risk level sums: %d" % sum(risklevel))