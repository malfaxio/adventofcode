#!/usr/bin/env python3

import re
import sys

class Reactor:
    def __init__(self):

        self.reactor = [[ [0 for x in range(-50,51)] for y in range(-50,51)] for z in range(-50,51)]

        print(len(self.reactor))
    
    def set(self, x1, x2, y1, y2, z1, z2, status):
        print("%s %d %d %d %d %d %d" % (status, x1, x2, y1, y2, z1, z2))

        if status == "on":
            st = 1
        else:
            st = 0

        for z in range(x1,x2+1):
            for y in range(y1, y2+1):
                for x in range(z1, z2+1):
                    # if (x >= -50 and x <= 50) and (y >= -50 and y <= 50) and (z >= -50 and z <= 50):
                    self.reactor[z][y][x] = st
        
    def norm(self, a, b):
        if a < -50:
            if b > 50:
                a = -50
                b = 50
            elif b >= -50:
                a = -50
            
        if b > 50:
            if a < -50:
                a = -50
                b = 50
            elif a >= -50:
                b = 50

        return (a, b)

    def count(self):
        c = 0
        for z in range(-50, 51):
            for y in range(-50, 51):
                for x in range(-50, 51):
                    if self.reactor[z][y][x] == 1:
                        c += 1

        return c


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    r = Reactor()

    for l in lines:
        # on x=-20..26,y=-36..17,z=-47..7
        print("L: %s " % l)
        m = re.search("(\w+)\s+x=(\-?\d+)\.\.(\-?\d+),y=(\-?\d+)\.\.(\-?\d+),z=(\-?\d+)\.\.(\-?\d+)", l)
        status = m.group(1)
        x1 = int(m.group(2))
        x2 = int(m.group(3))
        y1 = int(m.group(4))
        y2 = int(m.group(5))
        z1 = int(m.group(6))
        z2 = int(m.group(7))
        (x1, x2) = r.norm(x1,x2)
        (y1, y2) = r.norm(y1,y2)
        (z1, z2) = r.norm(z1,z2)
        if (-50 <= x1 <= 50) and (-50 <= x2 <= 50) and (-50 <= y1 <= 50) and (-50 <= y2 <= 50) and (-50 <= z1 <= 50) and (-50 <= z2 <= 50):
            r.set(x1, x2, y1, y2, z1, z2, status)
    
    print("count on: %d" % r.count())