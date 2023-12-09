#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re
import math


if __name__ == '__main__':
    lines = utils.aoc_read_bysection("fs.txt")

    path = [x for x in lines[0][0][:]]
    graph = {}
    for l in lines[1]:
        e = re.findall('(\w+) = \((\w+), (\w+)\)', l)
        graph[e[0][0]] = (e[0][1], e[0][2])
    
    pos = []
    for g in graph.keys():
        if g[2] == 'A':
            pos.append(g)
    print(pos)

    steps = []
    for pp in pos:
        print(pp)

        s = 0
        p = pp
        while p[2] != 'Z':
            d = path[s%len(path)]
            if d == 'L':
                p = graph[p][0]
            else:
                p = graph[p][1]

            s += 1
        
        steps.append(s)
        print(s)
    
    print(math.lcm(*steps))
