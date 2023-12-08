#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re

if __name__ == '__main__':
    lines = utils.aoc_read("fs.txt")

duration = [int(x) for x in re.findall("(\d+)", lines[0])]
distance = [int(x) for x in re.findall("(\d+)", lines[1])]

r = 1
for i in range(len(duration)):
    winh = []
    print(f"Duration: {duration[i]} Distance: {distance[i]}")
    for holding in range(duration[i]):
        ds = holding*(duration[i]-holding)
        if ds > distance[i]:
            winh.append(holding)
    print(winh)
    r *= len(winh)

print(r)

