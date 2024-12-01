#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils

def mapPrint(m):
    print()
    for y in m:
        print(''.join([str(s) for s in y]))

if __name__ == '__main__':
    dirs = {0: (1,0), 90: (0,1), 180: (-1,0), 270: (0,-1)}

    map = utils.aoc_read_asmap("fs.txt")
    ene = []
    for y in map:
        ene.append([0 for x in y])

    ray = [[0,0,0]]
    trail = []
    step = 0
    while len(ray) > 0:
        print(ray)
        nr = []
        for r in ray:
            (x, y, d) = r
            
            print(x,y,d)
            if 0 <= x < len(map[0]) and 0 <= y < len(map) and [x,y,d] not in trail:
                trail.append([x,y,d])
                ene[y][x] = 1
                if map[y][x] == '|' and d in [0, 180]:
                    nr.append([x, y-1, 270])
                    nr.append([x, y+1, 90])
                elif map[y][x] == '-' and d in [90, 270]:
                    nr.append([x-1, y, 180])
                    nr.append([x+1, y, 0])
                elif map[y][x] == '\\':
                    m1 = {0: 90, 90: 0, 180: 270, 270: 180}
                    (dx, dy) = dirs[m1[d]]
                    nr.append([x+dx, y+dy, m1[d]])
                elif map[y][x] == '/':
                    m2 = {0: 270, 90: 180, 180: 90, 270: 0 }
                    (dx, dy) = dirs[m2[d]]
                    nr.append([x+dx, y+dy, m2[d]])
                else:
                    (dx, dy) = dirs[d]
                    nr.append([x+dx, y+dy, d])
        ray = nr
        step += 1
    print(step)
    mapPrint(map)
    mapPrint(ene)
    s = 0
    for e in ene:
        for c in e:
            if c == 1:
                s += 1
    print(s)