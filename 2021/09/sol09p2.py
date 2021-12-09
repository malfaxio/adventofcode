#!/usr/bin/env python3

import sys

basins = []
deeps = []
max_x = max_y = 0

def notWall(x, y):
    global deeps

    r = True
    if x > (max_x-1) or x < 0 or y > (max_y-1) or y < 0:
        r = False
    elif deeps[y][x] == "9":
        r = False
    
    return r


def notHere(bt, bs, x, y):
    r = True
    for b in bt:
        if (b[0] == x) and (b[1] == y):
            r = False
            break
    
    for b in bs:
        if (b[0] == x) and (b[1] == y):
            r = False
            break

    return r


def notInBasins(x, y):
    global basins

    r = True
    for basin in basins:
        for c in basin:
            if (c[0] == x and c[1] == y):
                r = False
                break
    
    return r


def discoverBasin(sx, sy):
    global deeps

    print("Seed: %d %d" % (sx, sy))
    bt = [[sx, sy, 4]]
    iter = 1
    while(iter > 0):
        bs = []
        for b in bt:

            if b[2] > 0:
                if notWall(b[0], b[1]-1):
                    if notHere(bt, bs, b[0], b[1]-1):
                        bs.append([b[0], b[1]-1, 4])
                    b[2] -= 1
                else:
                    b[2] -= 1

                if notWall(b[0], b[1]+1):
                    if notHere(bt, bs, b[0], b[1]+1):
                        bs.append([b[0], b[1]+1, 4])
                    b[2] -= 1
                else:
                    b[2] -= 1

                if notWall(b[0]-1, b[1]):
                    if notHere(bt, bs, b[0]-1, b[1]):
                        bs.append([b[0]-1, b[1], 4])
                    b[2] -= 1
                else:
                    b[2] -= 1

                if notWall(b[0]+1, b[1]):
                    if notHere(bt, bs, b[0]+1, b[1]):
                        bs.append([b[0]+1, b[1], 4])
                    b[2] -= 1
                else:
                    b[2] -= 1

            bs.append(b)

        iter = 0
        for b in bs:
            if b[2] > 0:
                iter += 1
        
        bt = bs.copy()

    return bs


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    deeps = open(sys.argv[1]).read().splitlines()

    max_y = len(deeps)
    max_x = len(deeps[0])

    for y in range(len(deeps)):
        for x in range(len(deeps[y])):
            if notInBasins(x, y) and deeps[y][x] != "9":
                b = discoverBasin(x, y)
                if len(b) > 0:
                    basins.append(b)
    
    locs = []
    for basin in basins:
        locs.append(len(basin))

    locs.sort(reverse=True)

    print("Result: %d" % (locs[0]*locs[1]*locs[2]))
