#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re
from collections import Counter

value = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7 , '6': 6, '5': 5, '4': 4, '3': 3, '2': 2 }

def rank(cards):
    x = Counter(cards)
    t = Counter(x.values())
    r = 1
    if 5 in t:
        r = 7
    elif 4 in t:
        r = 6
    elif 3 in t and 2 in t:
        r = 5
    elif 3 in t:
        r = 4
    elif 2 in t:
        if t[2] > 1:
            r = 3
        else:
            r = 2

    return r

def sortOnRank(c):
    return c[1]


if __name__ == '__main__':
    lines = utils.aoc_read("fs.txt")

    ranked = []
    for l in lines:
        (cards, b) = l.split(" ")
        # cards = [x for x in c[:]]
        cards = cards.translate(str.maketrans(({'A': 'E', 'K': 'D', 'Q': 'C', 'J': 'B', 'T': 'A'})))
        ranked.append((cards, rank(cards), int(b)))

    ranked.sort()
    ranked.sort(key=sortOnRank)
    
    s = 0
    for r in range(len(ranked)):
        s += ranked[r][2] * (r+1)

    print(s)