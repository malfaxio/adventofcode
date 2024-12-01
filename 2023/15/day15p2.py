#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re

def hash(s):
    v = 0
    for c in s[:]:
        v += ord(c)
        v *= 17
        v %= 256
        
    return v

if __name__ == '__main__':
    lines = utils.aoc_read("fs.txt")

    box = {}
    # for i in range(256):
    #     box.append(())
    
    v = 0
    for s in lines[0].split(','):
        print(s)
        r = re.findall("(\w+)(=|-)(\d)*",s)
        label = r[0][0]
        op = r[0][1]
        v = r[0][2]
        i = hash(label)
        if op == '=':
            if i in box:
                box[i][label] = int(v)
            else:
                box[i] = {label:int(v)}
        elif op =='-':
            if i in box:
                if label in box[i]:
                    box[i].pop(label)
                    print('-')
        print(box)

    t = 0
    for b in box:
        c = 1
        for b1 in box[b]:
            t += (b+1) * c * box[b][b1]
            c += 1

    print(t)