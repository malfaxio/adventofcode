#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils

def distance(c1,c2):
    return abs(c2[0]-c1[0])+abs(c2[1]-c1[1])

if __name__ == '__main__':
    lines = utils.aoc_read("fs.txt")

    d = 1000000

    galaxies = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                galaxies.append((x,y))

    y0 = []
    for y in range(len(lines)):
        s = 0
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                s += 1
        if s == 0:
            y0.append(y)

    x0 = []
    for x in range(len(lines[0])):
        s = 0
        for y in range(len(lines)):
            if lines[y][x] == '#':
                s += 1
        if s == 0:
            x0.append(x)

    x0.reverse()
    y0.reverse()

    for i in range(len(x0)):
        g = []
        for j in range(len(galaxies)):
            if galaxies[j][0] > x0[i]:
                g.append((galaxies[j][0] + d-1, galaxies[j][1]))
            else:
                g.append(galaxies[j])
        galaxies = g
    for i in range(len(y0)):
        g = []
        for j in range(len(galaxies)):
            if galaxies[j][1] > y0[i]:
                g.append((galaxies[j][0], galaxies[j][1] + d-1))
            else:
                g.append(galaxies[j])
        galaxies = g

    dis = []
    for i in range(len(galaxies)):
        for g in galaxies[i+1:]:
            d = distance((galaxies[i][0], galaxies[i][1]), (g[0], g[1]))
            dis.append(d)
            
    print(sum(dis))

    # 82000210 low