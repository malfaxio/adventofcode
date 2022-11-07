#!/usr/bin/env python3

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

        return t

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    paths = Graph()
    for l in open(sys.argv[1]).read().splitlines():
        paths.add(l)

    paths.revela()

    print(paths.dfs("start", "end"))