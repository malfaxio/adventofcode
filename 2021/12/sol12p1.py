#!/usr/bin/env python3

import collections
import sys

class Graph:
    def __init__(self):
        self.g = {}
    
    def add(self, f, t):
        if f in self.g:
            self.g[f].append(t)
        else:
            self.g[f] = [t]            

        if t in self.g:
            self.g[t].append(f)
        else:
            self.g[t] = [f]

    def marked(self, n):
        print(n)

    def dfs(self, s, e):
        seen, queue = set([s]), collections.deque([s])

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


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    paths = Graph()
    for l in open(sys.argv[1]).read().splitlines():
        (f, t) = l.split("-")
        paths.add(f, t)

    print(paths.dfs("start", "end"))