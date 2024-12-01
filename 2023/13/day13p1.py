#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils

def findHorizontal(map):
    seeds = []
    for y in range(len(map)-1):
        if map[y] == map[y+1]:
            seeds.append([y, y+1])

    #seeds.sort()
    print("seeds:" + str(seeds))

    sym = []
    if len(seeds) > 0:
        for s in seeds:
            l = 0
            for i in range(len(map)):
                if ((s[0]-i) >= 0) and ((s[1]+i) < len(map)):
                    if map[s[0]-i] != map[s[1]+i]:
                        break
                l += 1
            if len(map) == l:
                sym = [s[0]+1, s[1]+1, l, len(map)]
                break
        print(sym)

    return sym

def findVertical(map):
    sym = findHorizontal([''.join(s) for s in zip(*map)])

    return sym

if __name__ == '__main__':
    maps = utils.aoc_read_bysection("fs.txt")

    i = 0
    s = 0
    for map in maps:
        print(f"Iter: {i}")
        i += 1
        hs = findHorizontal(map)
        if len(hs) > 0:
            print(f"H: {hs[0]}")
            s += hs[0]*100
        else:
            vs = findVertical(map)
            if len(vs) > 0:
                print(f"V: {vs[0]}")
                s += vs[0]
        
        
    print(s)
