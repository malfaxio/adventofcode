#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils

def findS(m):
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == 'S':
                break
        if m[y][x] == 'S':
            break
    
    return x, y

def get(m, x, y):
    rx = x % len(m[0])
    ry = y % len(m)

    return m[ry][rx]

def getNextPos(m, x, y):
    n = []
    for (dx, dy) in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
        if get(m, x+dx, y+dy) in ('.', 'S'):
            n.append([x+dx, y+dy])

    return n

def printPos(m, po):
    print()
    for y in range(len(m)):
        for x in range(len(m[y])):
            if [x,y] in po:
                print('O', end="")
            else:
                print(m[y][x], end="")
        print()

if __name__ == '__main__':
    map = utils.aoc_read_asmap("fs.txt")

    (x,y) = findS(map)
    pos = [(x,y)]
    for s in range(64):
        print(s+1)
        npos = []
        for (x,y) in pos:
            for n in getNextPos(map, x,y):
                if n not in npos:
                    npos += [n]
        pos = npos

    print(len(pos))