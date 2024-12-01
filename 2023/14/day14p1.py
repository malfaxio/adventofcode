#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils

def mapPrint(map):
    for y in map:
        print(''.join([s for s in y]))

def mapTilt(map):
    mv = 1
    while mv > 0:
        mv = 0
        for y in range(1,len(map)):
            for x in range(len(map[y])):
                if map[y][x] == 'O' and map[y-1][x] == '.':
                    map[y-1][x] = 'O'
                    map[y][x] = '.'
                    mv += 1
    return map

if __name__ == '__main__':
    map = utils.aoc_read_asmap("fs.txt")
    mapPrint(map)
    mapTilt(map)
    print()
    mapPrint(map)

    s = 0
    for y in range(len(map)):
        c = 0
        for x in range(len(map[y])):
            if map[y][x] == 'O':
                c += 1
        s += (len(map)-y)*c

    print(s)