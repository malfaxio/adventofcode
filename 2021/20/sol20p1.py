#!/usr/bin/env python3

from collections import *
import sys

class Image:
    def __init__(self, lines):
        self.grid = defaultdict(lambda: ".")
        self.algo = lines[0]
        image = list(map(list, lines[2:]))
        for y in range(len(image)):
            for x in range(len(image[0])):
                self.grid[y, x] = image[y][x]

    def trans(self, x, y):
        i = self.getIndex(x,y)

        return self.algo[i]

    def getIndex(self, x, y):
        s = ""
        for yc in [-1, 0, 1]:
            for xc in [-1, 0, 1]:
                if self.grid[y+yc, x+xc] == ".":
                    s += "0"
                else: 
                    s += "1"

        return int(s, 2)

    def refine(self, iter):
        f = False

        for _ in range(iter):
            # if not f:
            #     self.ngrid = defaultdict(lambda: '#')
            # else:
            self.ngrid = defaultdict(lambda: '.')
            min_x = min(x for x, y in self.grid.keys())
            max_x = max(x for x, y in self.grid.keys())
            min_y = min(y for x, y in self.grid.keys())
            max_y = max(y for x, y in self.grid.keys())
            for x in range(min_x - 1, max_x + 2):
                for y in range(min_y - 1, max_y + 2):
                    self.ngrid[y, x] = self.trans(x, y)
            
            self.grid = self.ngrid.copy()
            f = not f
            self.print()

        return self.grid

    def print(self):
        minx = min(x for x, y in self.grid.keys())
        maxx = max(x for x, y in self.grid.keys())
        miny = min(y for x, y in self.grid.keys())
        maxy = max(y for x, y in self.grid.keys())
        for y in range(miny-1, maxy+2):
            for x in range(minx-1, maxx+2):
                print(self.grid[y, x], end="")
            print()
        print()    
    
    def count(self):
        t = 0
        minx = min(x for x, y in self.grid.keys())
        maxx = max(x for x, y in self.grid.keys())
        miny = min(y for x, y in self.grid.keys())
        maxy = max(y for x, y in self.grid.keys())
        for y in range(miny-1, maxy+2):
            for x in range(minx-1, maxx+2):
                if self.grid[y, x] == "#":
                    t += 1
        
        return t

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    lines = open(sys.argv[1]).read().splitlines()

    img = Image(lines)

    img.print()

    i = img.refine(2)

    print(img.count())
