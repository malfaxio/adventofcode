#!/usr/bin/env python3

import re
import sys

dirtree = { '/': {} }
gblSum = 0


def setSize(path, s):
    global dirtree

    d = dirtree
    for p in path:
        d = d[p]

    d['__size'] = s


def calcSize(dt):
    global gblSum
    s = dt['__size']
    for p in dt:
        if p != '__size':
            s += calcSize(dt[p])
        print(p)

    print('Size %d' % s)
    if s <= 100000:
        gblSum += s

    return s


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    p1 = re.compile("^\$\s+(\w+)(?:\s+([\/\.\w]+))?$")
    p2 = re.compile("(\d+)\s\w")
    p3 = re.compile("^dir\s(.+)$")
    i = 0
    path = []
    while  i < len(lines):
        if lines[i][0] == '$':
            j = 1
            (cmd, param) = re.findall(p1, lines[i])[0]
            match cmd:
                case 'cd':
                    if param == '/':
                        path = [ '/' ]
                        parent = dirtree['/']
                    elif param == '..':
                        path.pop()
                        parent = dirtree
                        for p in path:
                            parent = parent[p]
                    else:
                        path.append(param)
                        parent = parent[param]
                case 'ls':
                    j = 0
                    s = 0
                    for l in lines[i+1:]:
                        if l[0] != '$':
                            if l[0:3] != 'dir':
                                m = re.match(p2, l)
                                s += int(m.group(1))
                            else:
                                m = p3.match(l)
                                parent[m.group(1)] = {}

                            j += 1
                        else:
                            setSize(path, s)
                            break
                    i = i + j - 1
        i += 1
    setSize(path, s)

    calcSize(dirtree['/'])
    print(gblSum)