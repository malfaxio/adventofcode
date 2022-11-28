#!/usr/bin/env python3

import sys

class Map:
    def __init__(self, lines):
        # Create map
        self.map = []
        self.mapnew = []
        self.mapold = []
        self.max_y = len(lines)
        self.max_x = len(lines[0])
        for y in range(self.max_y):
            self.map.append([a for a in lines[y]])
            self.mapnew.append([a for a in lines[y]])
            self.mapold.append(["0" for a in lines[y]])

    def print(self):
        print("Max X: %d" % self.max_x)
        print("Max Y: %d" % self.max_y)
        for y in self.map:
            for x in y:
                print(x, end="")
            print("")
    
    def copy(self, m1, m2):
        for y in range(self.max_y):
            for x in range(self.max_x):
                m1[y][x] = m2[y][x]
    
    def equal(self, m1, m2):
        ret = True
        for y in range(self.max_y):
            for x in range(self.max_x):
                if m1[y][x] != m2[y][x]:
                    ret = False
                    break

        return ret

    def step(self, e = True, s = True):
        # to East
        if e:
            for y in range(self.max_y):
                for x in range(self.max_x):
                    if self.get(x,y) == ">":
                        if self.get(x+1,y) == ".":
                            self.set(x,y,".")
                            self.set(x+1,y,">")

        self.copy(self.map, self.mapnew)

        # to Sud
        if s:
            for y in range(self.max_y):
                for x in range(self.max_x):
                    if self.get(x,y) == "v":
                        if self.get(x,y+1) == ".":
                            self.set(x,y,".")
                            self.set(x,y+1,"v")

        self.copy(self.map, self.mapnew)
        if self.equal(self.map, self.mapold):
            return False
        else:
            self.copy(self.mapold, self.map)
            return True
    
    def get(self, x, y):
        if x >= self.max_x:
            x = 0
        if y >= self.max_y:
            y = 0

        return self.map[y][x]

    def set(self, x, y, c):
        if x >= self.max_x:
            x = 0
        if y >= self.max_y:
            y = 0
        self.mapnew[y][x] = c

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    # Create map
    map = Map(lines)

    map.print()

    i = 1
    while map.step():
        print("Step: %d" % i)
        i += 1
    else:
        print("Step: %d" % i)