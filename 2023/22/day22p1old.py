#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re

def canFallTo(brk):
    global bricks
    global nbricks

    x1, y1, z1 = brk[0]
    x2, y2, z2 = brk[1]
    z = z1
    while z-1 > 1:
        block = False
        if z-1 in nbricks:
            for [[bx1, by1, bz1], [bx2, by2, bz2]] in nbricks[z-1]:
                for y in range(y1, y2+1):
                    for x in range(x1, x2+1):
                        if bx1 <= x <= bx2 and by1 <= y <= by2:
                            block = True
                            break
                    if block:
                        break
                if block:
                    break
        if block:
            break

        z -= 1
    
    return z1-z


if __name__ == '__main__':
    lines = utils.aoc_read("ts.txt")

    # reading bricks coords
    bricks = {}
    for l in lines:
        c1,c2 = l.split('~')
        x1,y1,z1 = [int(t) for t in c1.split(',')]
        x2,y2,z2 = [int(t) for t in c2.split(',')]
        if z1 not in bricks:
            bricks[z1] = [[(x1,y1,z1), (x2,y2,z2)]]
        else:
            bricks[z1].append([(x1,y1,z1), (x2,y2,z2)])

    bricks = dict(sorted(bricks.items()))
    print(bricks)
    nbricks = {}
    for z, brks in bricks.items():
        if z > 1:
            for b in brks:
                zt = canFallTo(b)
                print(zt)
                if z-zt in nbricks:
                    nbricks[z-zt].append(b)
                else:
                    nbricks[z-zt] = [b]
                print(zt)
        else:
            nbricks[z] = bricks[z]
    print(nbricks)