#!/usr/bin/env python3

import re
import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    p1 = re.compile("move (\d+) from (\d+) to (\d+)")

    # load all the data
    hflag = True
    header = []
    instr = []
    for l in lines:
        if hflag:
            if l != "":
                header.append(l)
            else:
                hflag = False
        else:
            m = p1.match(l)
            instr.append([int(m.group(1)), int(m.group(2)), int(m.group(3))])
    
    # crate composition
    p2 = re.compile("(\d+)")
    nstacks = None
    for r in re.findall(p2, header[-1]):
        if nstacks == None:
            nstacks = int(r)
        else:
            if int(r) > nstacks:
                nstacks = int(r)

    reg = "^"
    for i in range(nstacks-1):
        reg += "(?:\[([A-Z])\]|\s{3})\s"
    reg += "(?:\[([A-Z])\]|\s{3})$"

    p3 = re.compile(reg)
    stacks = []
    for i in range(nstacks):
        s = []
        for h in header[0:-1]:
            t = re.findall(p3, h)[0][i]
            if t != '':
                s.insert(0, t)
        stacks.append(s)

    for ins in instr:
        t = []
        for i in range(ins[0]):
            t.insert(0, stacks[ins[1]-1].pop())
        stacks[ins[2]-1].extend(t)

    s = ""
    for st in stacks:
        s += st[-1]
    print(s)
