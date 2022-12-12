#!/usr/bin/env python3

import re
import sys

ht = [ [0, 0] ]
tt = [ [0, 0] ]
utt = []

def checkHeadContact(xt, yt, xh, yh):
    r = False
    print(xt, yt, xh, yh)
    if abs(xh - xt) <= 1 and abs(yh - yt) <= 1:
        r = True
    print(r)
    return r

def draw():
    global ht, tt

    minx = maxx = miny = maxy = 0
    for t in ht:
        if t[0] < minx:
            minx = t[0]
        if t[0] > maxx:
            maxx = t[0]
        if t[1] < miny:
            miny = t[0]
        if t[1] > maxy:
            maxy = t[0]

    map = []
    for y in range(maxy-miny+1):
        m = []
        for x in range(maxx-minx+1):
            m.append('.')
        # y1 y
        #  2 0
        #  1 1
        #  0 2
        # -1 3
        #
        #  x1 -3 -2 -1 0 1 2 3 4 5
        #  x   0  1  2 3 4 5 6 7 8
        y1 = maxy - y
        for x in range(maxx-minx+1):
            x1 = maxx - x
            if [x1, y1] == ht[-1]:
                m[x] = 'H'
            elif [x1, y1] == tt[-1]:
                m[x] = 'T'
            elif [x1, y1] == [0, 0]:
                m[x] = 's'

        map.append(m)
    
    for m in map:
        for c in m[::-1]:
            print(c, end='')
        print('')

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    xh = yh = xt = yt = 0
    for l in lines:
        print(l)
        (d, s) = l.split(' ')
        for i in range(int(s)):
            match d:
                case 'U':
                    yh += 1
                case 'D':
                    yh -= 1
                case 'L':
                    xh -= 1
                case 'R':
                    xh += 1
            ht.append([xh, yh])
            if not checkHeadContact(xt, yt, xh, yh):
                # need to move T
                if yh > yt:
                    yt += 1
                if yh < yt:
                    yt -= 1
                if xh > xt:
                    xt += 1
                if xh < xt:
                    xt -= 1
                tt.append([xt, yt])
                if [xt, yt] not in utt:
                    utt.append([xt, yt])
            #draw()

    print(utt)
    print(len(utt))