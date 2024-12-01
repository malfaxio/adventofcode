#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils

def hash(s):
    v = 0
    for c in s[:]:
        v += ord(c)
        v *= 17
        v %= 256
        
    return v

if __name__ == '__main__':
    lines = utils.aoc_read("fs.txt")
    
    v = 0
    for s in lines[0].split(','):
        print(s)
        v += hash(s)
    print(v)