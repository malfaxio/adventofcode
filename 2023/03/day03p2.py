#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re

lines = utils.aoc_read("fs.txt")

def findPartNumbers(x, y):
    p = []
    # on the same row
    for m in re.finditer(r"\d+", lines[y]):
        if m.start()-1 <= x <= m.end():
            p.append(int(m.group(0)))
    if y > 0:
        for m in re.finditer(r"\d+", lines[y-1]):
            if m.start()-1 <= x <= m.end():
                p.append(int(m.group(0)))
    if y < len(lines):
        for m in re.finditer(r"\d+", lines[y+1]):
            if m.start()-1 <= x <= m.end():
                p.append(int(m.group(0)))
    
    return p

s = 0
for y in range(len(lines)):
    parts = []
    for x in range(len(lines[0])):
        if lines[y][x] == '*':
            print(lines[y][x], x, y)
            
            parts = findPartNumbers(x,y)
            if len(parts) == 2:
                s += parts[0]*parts[1]


print(s)