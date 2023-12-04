#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re

lines = utils.aoc_read("fs.txt")

tp = 0
for l in lines:
    print(l.split(':')[1].split('|')[0])
    winning = re.findall('(\d+)', l.split(':')[1].split('|')[0])
    extract = re.findall('(\d+)', l.split(':')[1].split('|')[1])

    p = 0
    for e in extract:
        if e in winning:
            if p == 0:
                p = 1
            else:
                p *= 2
    tp += p

print("Point: %d" % tp)