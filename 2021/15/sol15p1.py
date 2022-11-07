#!/usr/bin/env python3

import sys
<<<<<<< HEAD
=======
<<<<<<< HEAD
import heapq
>>>>>>> main

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

<<<<<<< HEAD
if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    m = Maze()
    for l in open(sys.argv[1]).read().splitlines():
        m.add(l)
    print(m.revela())

    vis = [[0] * len(row) for row in m.revela()]
    print(vis)
=======
if __name__ == '__main__':
    main()
=======

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()
    
    p = re.compile("([A-Z]+)\s->\s([A-Z])")

 
>>>>>>> 592ad0d5d3150f85712c98ee36d2530362fb619a
>>>>>>> main
