#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    mx = len(lines[0])
    my = len(lines)

    # Init map
    map = []
    for y in range(my):
        l = []
        for x in range(mx):
            l.append(int(lines[y][x]))
        map.append(l)

    # Init visibility matrix
    vis = []
    t = []
    for c in range(mx):
        t.append(1)
    vis.append(t)
    for l in map[1:-1]:
        t = [1]
        for c in l[1:-1]:
            t.append(0)
        t.append(1)
        vis.append(t)
    t = []
    for c in range(mx):
        t.append(1)
    vis.append(t)

    maxc = 0
    topCoord = []
    # Find best place
    for y in range(my):
        for x in range(mx):
            ct = cd = cl = cr = 0
            # Check top
            dy = y - 1
            while dy >=0:
                if map[y][x] > map[dy][x]:
                    ct += 1
                elif map[y][x] <= map[dy][x]:
                    ct += 1
                    break
                dy -= 1
            # Check bottom
            dy = y + 1
            while dy < my:
                if map[y][x] > map[dy][x]:
                    cd += 1
                elif map[y][x] <= map[dy][x]:
                    cd += 1
                    break
                dy += 1
            # Check left
            dx = x - 1
            while dx >= 0:
                if map[y][x] > map[y][dx]:
                    cl += 1
                if map[y][x] <= map[y][dx]:
                    ct += 1
                    break
                dx -= 1
            # CHeck right
            dx = x + 1
            while dx < mx:
                if map[y][x] > map[y][dx]:
                    cr += 1
                elif map[y][x] <= map[y][dx]:
                    cr += 1
                    break
                dx += 1
            if (ct * cd * cl * cr) > maxc:
                maxc = ct * cd * cl * cr
                topCoord.append([x, y, maxc])
    print(maxc)
    print(topCoord)