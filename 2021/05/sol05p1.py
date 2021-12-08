#!/usr/bin/env python3

import sys
import re

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    f = open(sys.argv[1])
    lines = f.readlines()

    extractions = lines[0].split(",")

    p = re.compile("(\d+),(\d+)\s->\s(\d+),(\d+)")

    # check board size
    mx = my = 0
    segments = []
    for l in lines:
        m = p.match(l)
        x1 = int(m.group(1))
        y1 = int(m.group(2))
        x2 = int(m.group(3))
        y2 = int(m.group(4))
        if x1 > mx:
            mx = x1
        if x2 > mx:
            mx = x2
        if y1 > my:
            my = y1
        if y2 > my:
            my = y2
        segments.append([x1, y1, x2, y2])
    
    boards = []
    # init board
    for y in range(my+1):
        xr = []
        for x in range(mx+1):
            xr.append(0)
        boards.append(xr)

    # fill board
    for s in segments:
        if (s[0] == s[2]) or (s[1] == s[3]):
            if s[2] > s[0]:
                x1=s[0]
                x2=s[2]
            else:
                x1=s[2]
                x2=s[0]
            if s[3] > s[1]:
                y1=s[1]
                y2=s[3]
            else:
                y1=s[3]
                y2=s[1]
        
            print("X1: %d Y1: %d -> X2: %d Y2: %d" % (x1, y1, x2, y2))
            for y in range(y1,y2+1):
                for x in range(x1,x2+1):
                    boards[y][x] = boards[y][x] + 1
    
    # check board
    c = 0
    for y in range(my+1):
        for x in range(mx+1):
            if boards[y][x] > 1:
                c = c +1
    
    print("Count: %d" % c)


