#!/usr/bin/env python3

import re
import sys

ht = [ [0, 0] ]
tt = []
ut = []

def checkHeadContact(xt, yt, xe, ye):
    r = False
    if abs(xe - xt) <= 1 and abs(ye - yt) <= 1:
        r = True

    return r


def draw():
    xo = 11
    yo = 15
    map = []
    for y in range(21):
        m = []
        for x in range(26):
            m.append('.')
        map.append(m)

    map[yo][xo] = 's'
    for t in range(8, -1, -1):
        x1 = xo+xtr[t]
        y1 = yo+ytr[t]
        map[y1][x1] = str(t+1)
    map[yo+yh][xo+xh] = 'H'

    for m in map:
        for c in m:
            print(c, end='')
        print('')


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
    
    xtr = []
    ytr = []
    for t in range(9):
        tt.append([0, 0])
        xtr.append(0)
        ytr.append(0)

    xh = yh = 0
    for l in lines:
        print(l)
        (d, s) = l.split(' ')
        for i in range(int(s)):
            match d:
                case 'U':
                    yh -= 1
                case 'D':
                    yh += 1
                case 'L':
                    xh -= 1
                case 'R':
                    xh += 1
            ht.append([xh, yh])
            xe = xh
            ye = yh
            for t in range(9): 
                xt = xtr[t]
                yt = ytr[t]
                if not checkHeadContact(xt, yt, xe, ye):
                    # need to move T
                    if ye > yt:
                        yt += 1
                    if ye < yt:
                        yt -= 1
                    if xe > xt:
                        xt += 1
                    if xe < xt:
                        xt -= 1
                    tt[t].append([xt, yt])
                xtr[t] = xt
                ytr[t] = yt
                xe = xt
                ye = yt
            # Just only of the last tail xt[8], yt[8]
            if [xt, yt] not in ut:
                ut.append([xt, yt])

    print(len(ut))