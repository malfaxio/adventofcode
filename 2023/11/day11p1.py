#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils

def distance(c1,c2):
    return abs(c2[0]-c1[0])+abs(c2[1]-c1[1])

if __name__ == '__main__':
    lines = utils.aoc_read("fs.txt")

    # expansion
    mt = []
    for y in range(len(lines)):
        mt.append(lines[y])
        s = 0
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                s += 1
        if s == 0:
            mt.append(lines[y])

    empty_cols = []
    for x in range(len(mt[0])):
        s = 0
        r = ""
        for y in range(len(mt)):
            if mt[y][x] == '#':
                s += 1
        if s == 0:
            empty_cols.append(x)
    
    universe = []
    for y in range(len(mt)):
        r = ""
        i = 0
        for e in empty_cols:
            r += mt[y][i:e+1]
            r += '.'
            i = e+1
        r += mt[y][i:]
        universe.append(r)

    galaxies = []
    for y in range(len(universe)):
        for x in range(len(universe[y])):
            if universe[y][x] == '#':
                galaxies.append((x,y))

    #print(utils.shortestPath(grid, [4,0], [9,10]))
    dis = []
    for i in range(len(galaxies)):
        for g in galaxies[i+1:]:
            d = distance((galaxies[i][0], galaxies[i][1]), (g[0], g[1]))
            dis.append(d)
            
    print(sum(dis))