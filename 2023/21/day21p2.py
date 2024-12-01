#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import math

def findS(m):
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == 'S':
                break
        if m[y][x] == 'S':
            break
    
    return x, y

def get(x, y):
    global map

    rx = x % len(map[0])
    ry = y % len(map)

    return map[ry][rx]

def getNextPos(x, y):
    global map

    n = []
    for (dx, dy) in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
        if get(x+dx, y+dy) in ('.', 'S'):
            n.append([x+dx, y+dy])

    return n

def printPos():
    global map
    global bitmap

    print()
    for y in range(len(map)):
        for x in range(len(map[y])):
            if len(bitmap[y][x]) > 0:
                print(str(len(bitmap[y][x])), end="")
            else:
                print(map[y][x], end="")
        print()

def posFromBitmap():
    global bitmap

    p = []
    for y in range(len(bitmap)):
        for x in range(len(bitmap[y])):
            for b in bitmap[y][x]:
                p.append(b)
    return p

def getSect(c):
    global map

    sx = math.floor(c[0]/len(map[0]))
    sy = math.floor(c[1]/len(map))

    return [sx, sy]

if __name__ == '__main__':
    map = utils.aoc_read_asmap("fs.txt")

    bitmap = [[[] for col in range(len(map[0]))] for row in range(len(map))]
    (x,y) = findS(map)
    bitmap[y][x] = [[x,y]]
    utils.mapPrint(bitmap)

    for s in range(26501365):
        print(s+1)
        pos = posFromBitmap()
        bitmap = [[[] for col in range(len(map[0]))] for row in range(len(map))]
        for (x,y) in pos:
            for n in getNextPos(x, y):
                rx = n[0] % len(map[0])
                ry = n[1] % len(map)
                if n not in bitmap[ry][rx]:
                    bitmap[ry][rx].append(n)

    s = 0
    for y in bitmap:
        for x in y:
            s += len(x)
    print(s)