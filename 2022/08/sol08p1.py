#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    mx = len(lines[0])
    my = len(lines)
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

    
    for x in range(1, mx-1):
        # Check from top
        m = map[0][x]
        for y in range(1,my-2):
            if map[y][x] > m:
                m = map[y][x]
                vis[y][x] = 1
        
        # Check from bottom
        m = map[-1][x]
        for y in range(my-2, 0, -1):
            if map[y][x] > m:
                m = map[y][x]
                vis[y][x] = 1

    for y in range(1, my-1):
        # Check from left
        m = map[y][0]
        for x in range(1, mx-2):
            if map[y][x] > m:
                m = map[y][x]
                vis[y][x] = 1
        
        # Check from right
        m = map[y][-1]
        for x in range(mx-2, 0, -1):
            if map[y][x] > m:
                m = map[y][x]
                vis[y][x] = 1

    c = 0
    for y in range(my):
        for x in range(mx):
            if vis[y][x] == 1:
                c += 1

    print(c)

