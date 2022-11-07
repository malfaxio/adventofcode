#!/usr/bin/env python3

import sys
import re

def navigate(node, visited = set()):
    t = 0
    print("Node: %s" % node)
    print(visited)
    if node == "end":
        return 1

    for v in vertex[node]:
        if v not in visited:
            t += navigate(v, visited | {node} if node == node.lower() else visited)
    return t
    

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    p = re.compile("([a-zA-Z]+)-([a-zA-Z]+)")

    vertex = {}
    for l in lines:
        m = p.match(l)
        a = m.group(1)
        b = m.group(2)
        vertex[a] = vertex.get(a, []) + [b]
        vertex[b] = vertex.get(b, []) + [a]

    print(vertex)

    t = navigate("start")
    print("Total: %d" % t)