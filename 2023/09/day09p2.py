#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re
from collections import Counter
from collections import deque  

def diff(l):
    d = []
    for i in range(len(l)-1):
        d.append(l[i+1]-l[i])

    return d

def check0(l):
    r = True
    for e in l:
        if e != 0:
            r = False
            break

    return r

def predict(hh):
    for j in range(len(hh)-2,0,-1):
        p = hh[j-1][-1]+hh[j][-1]
        hh[j-1].append(p)
    
    return hh[0][-1]

if __name__ == '__main__':
    lines = utils.aoc_read("fs.txt")

    p = 0
    for l in lines:
        h = [int(x) for x in l.split(" ")]
        h.reverse()
        
        hh = [ h ]
        all0 = False
        while True:
            d = diff(h)
            hh.append(d)
            if check0(d):
                all0 = True
                break
            h = d

        p += predict(hh)
    
    print(p)