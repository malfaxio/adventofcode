#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re

repls = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

lines = utils.aoc_read("set.txt")

n = 0
for l in lines:
    for r in repls:
        l = l.replace(r, repls[r])

    m = re.findall('(\d)', l)
    s = int(str(m[0])+str(m[-1]))
    n += s

print(n)