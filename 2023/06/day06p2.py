#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re
import math


if __name__ == '__main__':
    lines = utils.aoc_read("fs.txt")

    dur = re.findall("(\d+)", lines[0])
    dis = re.findall("(\d+)", lines[1])

    dis2 = ""
    dur2 = ""
    for i in range(len(dur)):
        dis2 += dis[i]
        dur2 += dur[i]
    duration = int(dur2)
    distance = int(dis2)

    print(duration, distance)

    s = 0
    for holding in range(duration):
            ds = holding*(duration-holding)
            if ds > distance:
                s += 1
            
    print(s)