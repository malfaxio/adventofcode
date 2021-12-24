#!/usr/bin/env python3

import sys
import re

def fold(dir, v):
    global dots

    print("Fold along %d %s" % (v, dir))
    my = len(dots)
    mx = len(dots[0])
    # y=...
    if dir == 'y':
        for y in range(v+1, my):
            yc = v-(y-v)
            for x in range(mx):
                if dots[y][x] == 1:
                    dots[yc][x] = dots[y][x]
                
            print("Y: %d to %d" % (y, yc))
        for y in range(v, my):
            print("Remove %d" % y)
            dots.pop()
    else:
        for y in range(my):
            for x in range(v+1,mx):
                xc = v-(x-v)
                if dots[y][x] == 1:
                    dots[y][xc] = dots[y][x]

            for x in range(v, mx):
                dots[y].pop()


def countDots():
    global dots

    c = 0
    for y in range(len(dots)):
        for x in range(len(dots[y])):
            if dots[y][x] == 1:
                c += 1
    return c


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    p = re.compile("(\d+),(\d+)|(fold)\salong\s(\S)=(\d+)")

    mx = -1
    my = -1
    folds = []
    for l in lines:
        m = p.match(l)
        if m is not None and m.group(3) == "fold":
            folds.append([m.group(4), int(m.group(5))])
        elif m is not None:
            if int(m.group(1)) > mx:
                mx = int(m.group(1))
            if int(m.group(2)) > my:
                my = int(m.group(2))

    dots = [[0 for i in range(mx+1)] for j in range(my+1)]

    for l in lines:
        m = p.match(l)
        if m is not None and m.group(1) is not None:
            dots[int(m.group(2))][int(m.group(1))] = 1

    for f in folds:
        fold(f[0], f[1])

    c = countDots()

    print("N. of dots: %d" % c)