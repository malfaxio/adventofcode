#!/usr/bin/env python3

<<<<<<< HEAD
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

=======
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
    
>>>>>>> 592ad0d5d3150f85712c98ee36d2530362fb619a

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

<<<<<<< HEAD
    paths = Graph()
    for l in open(sys.argv[1]).read().splitlines():
        (f, t) = l.split("-")
        paths.add(f, t)

    print(paths.dfs("start", "end"))
=======
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
>>>>>>> 592ad0d5d3150f85712c98ee36d2530362fb619a
