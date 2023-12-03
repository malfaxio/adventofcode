#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re

lines = utils.aoc_read("fs.txt")

red_limit = 12
green_limit = 13
blue_limit = 14

s = 0
for l in lines:
    m = re.match('^Game (\d+)', l)
    gid = int(m.group(1))

    red = [int(x) for x in re.findall('(\d+) red', l)]
    green = [int(x) for x in re.findall('(\d+) green', l)]
    blue = [int(x) for x in re.findall('(\d+) blue', l)]
    power = max(red) * max(green) * max(blue)

    s += power

print(s)