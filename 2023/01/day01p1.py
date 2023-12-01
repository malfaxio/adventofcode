#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re

lines = utils.aoc_read("set.txt")

#r = re.compile('^.*(\d).*(\d).*$')
n = 0
for l in lines:
    m = re.findall('(\d)', l)
    n += int(str(m[0])+str(m[-1]))

print(n)