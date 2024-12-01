#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
from math import inf

def solve(h1, h2):
    x1, y1, z1 = h1['p']
    v1x, v1y, v1z = h1['v']
    x2, y2, z2 = h2['p']
    v2x, v2y, v2z = h2['v']

    if v1y*v2x-v1x*v2y == 0: return inf, inf
    x = (v1x*v2x*(y2-y1)-v2y*v1x*x2+v1y*v2x*x1)/(v1y*v2x-v1x*v2y)
    y = (v1y*v2y*(x2-x1)-v2x*v1y*y2+v1x*v2y*y1)/(v1x*v2y-v1y*v2x)
    if v1x and (x-x1)/v1x < 0 or v2x and (x-x2)/v2x < 0: return inf, inf
    if v1y and (y-y1)/v1y < 0 or v2y and (y-y2)/v2y < 0: return inf, inf

    return x, y

if __name__ == '__main__':
    lines = utils.aoc_read("fs.txt")

    # reading bricks coords
    hailstones = []
    for l in lines:
        hailstones.append({'p': [int(x) for x in l.split('@')[0].split(',')], 'v': [int(x) for x in l.split('@')[1].split(',')]})

    print(hailstones)

    low = 200000000000000
    up  = 400000000000000
    res = 0
    for i in range(len(hailstones)):
        for j in range(i+1, len(hailstones)):
            x,y = solve(hailstones[i], hailstones[j])
            if low <= x <= up and low <= y <= up:
                print(x, y)
                print(hailstones[i], ' ', hailstones[j])
                res += 1

    print(res)