#!/usr/bin/env python3

import sys

class Maze:
    def __init__(self):
        self.maze = []

    def add(self, l):
        t = []
        for c in l:
            t.append(int(c))

        self.maze.append(t)

    def revela(self):
        return self.maze

    def solve(self):
        rows = len(self.maze)
        cols = len(self.maze)
    
    def solve(self):
        rows = len(self.maze)
        cols = len(self.maze[0])
        print([cols, rows])

        mincost = [[0] * len(row) for row in m.maze]
        for r in range(0, rows):
            for c in range(0, cols):
                mincost[c, r] = 

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    m = Maze()
    for l in open(sys.argv[1]).read().splitlines():
        m.add(l)

    m.solve()

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    m = Maze()
    for l in open(sys.argv[1]).read().splitlines():
        m.add(l)
    print(m.revela())

    vis = [[0] * len(row) for row in m.revela()]
    print(vis)