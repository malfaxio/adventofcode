#!/usr/bin/env python3

import re
import sys

class Monkey:

    def __init__(self, x):
        self.id = int(x[0])
        self.items = [int(i.strip()) for i in x[1].split(',')]
        self.operation = x[2]
        self.operand = x[3]
        self.divisible = int(x[4])
        self.truetarget = int(x[5])
        self.falsetarget = int(x[6])
        self.inspectCounter = 0

    def inspect(self):
        r = []
        for w in self.items:
            self.inspectCounter += 1
            # Calc new worry level
            if self.operand == "old":
                opr = w
            else:
                opr = int(self.operand)
            if self.operation == '*':
                nw = w * opr
            elif self.operation == '+':
                nw = w + opr

            # Relief
            nw /= 3

            if int(nw) % self.divisible != 0:
                # Not divisible, so false
                r.append([self.falsetarget, int(nw)])
            else:
                r.append([self.truetarget, int(nw)])

        self.items = []

        return r

    def receive(self, i):
        self.items.append(i)

    def status(self):
        print("Monkey %d:" % self.id, end='')
        for i in self.items:
            print(" %d" % i, end='')
        print()
    
    def activity(self):
        return self.inspectCounter


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    mons = []
    m = re.compile("Monkey (\d+):\s+Starting items: ([\s,\d]+)\s\sOperation: new = old (\*|\+) (\d+|old)\s+Test: divisible by (\d+)\s+If true: throw to monkey (\d+)\s+If false: throw to monkey (\d+)")
    data = ""
    for l in lines:
        if l != "":
            data += l
        else:
            mons.append(Monkey(m.findall(data)[0]))
            data = ""
    mons.append(Monkey(m.findall(data)[0]))

    for rn in range(20):
        for m in mons:
            its = m.inspect()
            for tm, i in its:
                mons[tm].receive(i)
            
        for m in mons:
            m.status()


    a = []
    for m in mons:
        a.append(m.activity())
    
    a.sort(reverse=True)
    print(a[0] * a[1])
    