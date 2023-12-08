#!/usr/bin/env python3

import sys
from collections import deque  

def getZ(x, y):
    global lines

    if lines[y][x] == 'S':
        z = ord('a')
    elif lines[y][x] == 'E':
        z = ord('z')
    else:
        z = ord(lines[y][x])
    
    return z

def availDir(x, y):
    global H
    global W
    global trails

    dt = []
    z = getZ(x, y)
    if x < (W-1):
        if (getZ(x+1, y) - z) <= 1:
            dt.append([x+1, y])
    if y < (H-1):
        if (getZ(x, y+1) - z) <= 1:
            dt.append([x, y+1])
    if x > 0:
        if (getZ(x-1, y) - z) <= 1:
            dt.append([x-1, y])
    if y > 0:
        if (getZ(x, y-1) - z) <= 1:
            dt.append([x, y-1])

    df = []
    for d in dt:
        if d not in trails:
            df.append(d)

    return df

def findPath(x, y):
    global trails

    singlePath = True
    sp = 0
    while(1==1):
        if lines[y][x] != 'E':
            nd = availDir(x,y)
            if len(nd) >= 1:
                for (xt, yt) in nd:
                    trails.append([xt,yt])
                    singlePath = False
                    findPath(xt, yt)
            elif len(nd) == 1:
                singlePath = True
                sp += 1
                x = nd[0][0]
                y = nd[0][1]
            else:
                for j in range(sp):
                    trails.pop(sp)
                sp = 0
        else:
            print("Found")
            singlePath = False
            print("Path: %d" % len(trails))
            
            return


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    H = len(lines)
    W = len(lines[0])

    x = y = 0
    print(lines)
    
    trails = deque()
    findPath(0,0)