#!/usr/bin/env python3

import re
import sys

class Reactor:
    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):

        self.reactor = {}
        self.xl      = (x_max-x_min)+1
        self.yl      = (y_max-y_min)+1
        self.zl      = (z_max-z_min)+1 

        print("Reactor size: %d x %d x %d" % (self.xl, self.yl, self.zl))
    
    def set(self, x, y, z, st):
        # change coord system
        x1 = x-x_min
        y1 = y-y_min
        z1 = z-z_min
        i = x1 + (y1 + z1 * self.yl) * self.xl
        if st == "on":
            self.reactor.update({i: 1})
        else:
            if i in self.reactor:
                self.reactor.pop(i)

    def turnCuboid(self, x1, x2, y1, y2, z1, z2, status):
        print("%s %d %d %d %d %d %d" % (status, x1, x2, y1, y2, z1, z2))

        for z in range(z1,z2+1):
            for y in range(y1, y2+1):
                if status == "on":
                    self.add(x1, x2, y, z)
                else:
                    self.sub(x1, x2, y, z)
    
    def add(self, x1, x2, y, z):
        i = y + z * self.yl

        if i in self.reactor:
            t = []
            aflag = True
            for e in self.reactor[i]:
                if x1 != e[0] and x2 != e[1]:
                    if (e[0] <= x1 <= e[1]) and x2 > e[1]:
                        aflag = False
                        t += [(e[0], x2)]
                    elif (e[0] <= x2 <= e[1] and x1 < e[0]):
                        aflag = False
                        t += [(x1, e[1])]
                    elif x1 < e[0] <= e[1] < x2:
                        aflag = False
                        t += [(x1, x2)]
                    else:
                        t += [(e[0], e[1])]
                else:
                    aflag = False
            if aflag == True:
                t += [(x1,x2)]
            
            self.reactor[i] = t
        else:
            self.reactor[i] = [(x1,x2)]

    def sub(self, x1, x2, y, z):
        i = y + z * self.yl

        if i in self.reactor:
            t = []
            aflag = True
            for e in self.reactor[i]:
                if x1 != e[0] and x2 != e[1]:
                    if (e[0] <= x1 <= e[1]) and x2 >= e[1]:
                        t += [(e[0], x1-1)]
                    elif (e[0] <= x2 <= e[1]) and x1 <= e[0]:
                        t += [(x2+1, e[1])]
                    elif e[0] < x1 <= x2 < e[1]:
                        t += [(e[0], x1-1), (x2+1, e[1])]
                    else:
                        t+= [(e[0], e[1])]

            self.reactor[i] = t

    def count(self):
        c = 0
        for i, r in self.reactor.items():
            for e in r:
                c += e[1]-e[0]+1

        return c


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    m     = re.search("(\w+)\s+x=(\-?\d+)\.\.(\-?\d+),y=(\-?\d+)\.\.(\-?\d+),z=(\-?\d+)\.\.(\-?\d+)", lines[0])
    x_min = int(m.group(2))
    x_max = int(m.group(3))
    y_min = int(m.group(4))
    y_max = int(m.group(5))
    z_min = int(m.group(6))
    z_max = int(m.group(7))  
    for l in lines[1:]:
        m = re.search("(\w+)\s+x=(\-?\d+)\.\.(\-?\d+),y=(\-?\d+)\.\.(\-?\d+),z=(\-?\d+)\.\.(\-?\d+)", l)
        if int(m.group(2)) < x_min:
            x_min = int(m.group(2))
        if int(m.group(3)) > x_max:
            x_max = int(m.group(3))
        if int(m.group(4)) < y_min:
            y_min = int(m.group(4))
        if int(m.group(5)) > y_max:
            y_max = int(m.group(5))
        if int(m.group(6)) < z_min:
            z_min = int(m.group(6))
        if int(m.group(7)) > z_max:
            z_max = int(m.group(7))

    print("%d %d %d %d %d %d" % (x_min, x_max, y_min, y_max, z_min, z_max))

    r = Reactor(x_min, x_max, y_min, y_max, z_min, z_max)

    print("Init")
    for l in lines:
        # on x=-20..26,y=-36..17,z=-47..7
        print("L: %s " % l)
        m      = re.search("(\w+)\s+x=(\-?\d+)\.\.(\-?\d+),y=(\-?\d+)\.\.(\-?\d+),z=(\-?\d+)\.\.(\-?\d+)", l)
        status = m.group(1)
        x1     = int(m.group(2))
        x2     = int(m.group(3))
        y1     = int(m.group(4))
        y2     = int(m.group(5))
        z1     = int(m.group(6))
        z2     = int(m.group(7))

        r.turnCuboid(x1, x2, y1, y2, z1, z2, status)
        print("c %d" % r.count())
    
    print("count on: %d" % r.count())