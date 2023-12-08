#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re

lines = utils.aoc_read("fs.txt")

def findPartNumbers(x, y):
    print(x,y)

    p = []
    # on the same row
    for m in re.finditer(r"\d+", lines[y]):
        print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
        if m.start()-1 <= x <= m.end():
            p.append(int(m.group(0)))
    if y > 0:
        for m in re.finditer(r"\d+", lines[y-1]):
            print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
            if m.start()-1 <= x <= m.end():
                p.append(int(m.group(0)))
    if y < len(lines):
        for m in re.finditer(r"\d+", lines[y+1]):
            print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
            if m.start()-1 <= x <= m.end():
                p.append(int(m.group(0)))
    
    return p

parts = []
for y in range(len(lines)):
    # finding symbols
    for x in range(len(lines[0])):
        if lines[y][x] != '.' and (lines[y][x] < '0' or lines[y][x] > '9'):
            print(lines[y][x], x, y)
            
            parts += findPartNumbers(x,y)
            print(parts)


print(sum(parts))