#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re

lines = utils.aoc_read("fs.txt")

tp = 0
cards = []
for l in lines:
    winning = re.findall('(\d+)', l.split(':')[1].split('|')[0])
    extract = re.findall('(\d+)', l.split(':')[1].split('|')[1])

    p = 0
    for e in extract:
        if e in winning:
            p += 1
    
    cards.append([p, 1])

for i in range(len(cards)):
    if cards[i][0] > 0:
        for w in range(cards[i][1]):
            for j in range(cards[i][0]):
                cards[i+j+1][1] += 1

p = 0
for c in cards:
    p += c[1]

print(p)