#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re
from collections import Counter
from collections import deque  


if __name__ == '__main__':
    lines = utils.aoc_read_bysection("ts.txt")

    path = [x for x in lines[0][0][:]]
    graph = {}
    for l in lines[1]:
        e = re.findall('(\w+) = \((\w+), (\w+)\)', l)
        graph[e[0][0]] = (e[0][1], e[0][2])
    
    print(path)
    print(graph)

    step = 0
    p = 'AAA'
    while p != 'ZZZ':
        d = path[step%len(path)]
        print(d)
        if d == 'L':
            p = graph[p][0]
        else:
            p = graph[p][1]

        step += 1


    print(step)