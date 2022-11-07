#!/usr/bin/env python3

import collections
import sys

class Graph:
    def __init__(self):
        self.g = {}

    def add(self, l):
        (f, t) = l.split("-")
        self.g[f] = self.g.get(f, []) + [t]
        self.g[t] = self.g.get(t, []) + [f]

    def revela(self):
        print(self.g)

    def dfs(self, s, e, v = set()):
        if s == e:
            return 1

        t = 0
        for n in self.g[s]:
            if n in v: continue
            print(v | {s} if s == s.lower() else v)
            t += self.dfs(n, e, v | {s} if s == s.lower() else v)

        while queue:
            vx = queue.popleft()
            self.marked(vx)
            for node in self.g[vx]:
                if node == e:
                    break
                if node in self.g[vx]:
                    if node not in seen:
                        seen.add(node)
                        queue.append(node)

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

    paths = Graph()
    for l in open(sys.argv[1]).read().splitlines():
        paths.add(l)

    paths.revela()

    print(paths.dfs("start", "end"))

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