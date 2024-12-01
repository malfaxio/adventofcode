#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re
from collections import Counter
from collections import deque  

def get(x, y):
    r = None
    if 0 <= x < len(lines[0]):
        if 0 <= y < len(lines):
            r = lines[y][x]

    return r

def findS():
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if get(x, y) == 'S':
                break
        if get(x, y) == 'S':
                break

    return (x,y)

def typeS(x,y):
    for t in ('|', '-', 'L', 'J', '7', 'F', None):
        if t == 'F' and (get(x+1, y) in ('-', 'J', '7')) and (get(x, y+1) in ('|', 'J', 'L')):
            break
        if t == '-' and (get(x-1, y) in ('-', 'L', 'F')) and (get(x+1, y) in ('-', 'J', '7')):
            break

    return t

def nextDir(x, y, trail):
    c = get(x,y)
    tx = trail[-2][0]
    ty = trail[-2][1]
    if c == 'F':
        if (x + 1) == tx and y == ty:
            rx = x
            ry = y + 1
        else:
            rx = x + 1
            ry = y
    elif c == 'J':
        if x == tx and (y - 1) == ty:
            rx = x-1
            ry = y
        else:
            rx = x
            ry = y - 1
    elif c == '|':
        if x == tx and (y - 1) == ty:
            rx = x
            ry = y + 1
        else:
            rx = x
            ry = y - 1
    elif c == 'L':
        if (x + 1) == tx and y == ty:
            rx = x
            ry = y - 1
        else:
            rx = x + 1
            ry = y
    elif c == '7':
        if (x - 1) == tx and y == ty:
            rx = x
            ry = y + 1
        else:
            rx = x - 1
            ry = y
    elif c == '-':
        ry = y
        if (x - 1) == tx:
            rx = x + 1
        else:
            rx = x - 1
    else:
        print(f"Miss: {c}")
        
    return rx, ry

def printLoop(t1, t2):
    map = []
    for i in range(len(lines)):
        l = []
        for j in range(len(lines[0])):
            l.append('.')
        map.append(l)
    
    # create the border
    for t in trail1+trail2:
        map[t[1]][t[0]] = get(t[0], t[1])

    # find inner
    ci = 0
    for y in range(len(map)):
        inn = False
        for x in range(len(map[0])):
            if map[y][x] in ('|', 'J', 'L') and inn == False:
                inn = True
            elif map[y][x] in ('|', 'J', 'L') and inn == True:
                inn = False

            if map[y][x] == '.' and inn == True:
                map[y][x] = '@'
                ci += 1

    for m in map:
        for c in m:
            print(c, end="")
        print("")
    
    print(ci)
    
if __name__ == '__main__':
    lines = utils.aoc_read("fs.txt")

    (x,y) = findS()
    t = typeS(x,y)
        
    if t == 'F':
        x1 = x+1
        y1 = y
        x2 = x
        y2 = y+1
    elif t == '-':
        x1 = x + 1
        y1 = y
        x2 = x - 1
        y2 = y
    trail1 = [(x,y)]
    trail2 = [(x,y)]
    f = False
    step = 0
    while f == False:
        c1 = get(x1,y1)
        c2 = get(x2,y2)
        if c1 == c2 and (x1 == x2) and (y1 == y2):
            print(f"Gotcha {step + 1}")
            f = True
        else:
            trail1.append((x1, y1))
            trail2.append((x2, y2))
            (x1, y1) = nextDir(x1, y1, trail1)
            (x2, y2) = nextDir(x2, y2, trail2)

        step += 1

    trail1.append((x1, y1))
    trail2.append((x2, y2))

    printLoop(trail1,trail2)
    