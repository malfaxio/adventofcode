#!/usr/bin/env python3

import sys

class Graph:
    def __init__(self):
        self.g = {}

    def add(self, l):
        (f, t) = l.split("-")
        self.g[f] = self.g.get(f, []) + [t]
        self.g[t] = self.g.get(t, []) + [f]

    def dfs(self, s, e, v = set(), d = False):
        if s == e:
            return 1
        
        t = 0
        for n in self.g[s]:
            if n == "start": continue
            if n in v and d: continue
            if n in v:
                t += self.dfs(n, e, v | {s} if s == s.lower() else v, True)
            else:
                t += self.dfs(n, e, v | {s} if s == s.lower() else v, d)

        return t

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    paths = Graph()
    for l in open(sys.argv[1]).read().splitlines():
        paths.add(l)

    print(paths.dfs("start", "end"))