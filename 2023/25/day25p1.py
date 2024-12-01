#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
from dataclasses import dataclass
from collections import defaultdict

import graphviz

@dataclass(frozen=True)
class Graph:
    edges: dict
    def add_edge(self, u, v):
        self.edges[u].add(v)
        self.edges[v].add(u)

    def remove_edge(self, u, v):
        self.edges[u].remove(v)
        self.edges[v].remove(u)

    def visualise(self):
        dot = graphviz.Graph(format='svg', engine='neato')
        for u, nbrs in self.edges.items():
            for v in nbrs:
                if u < v:
                    dot.edge(u, v)
        dot.render()

    def remove_node(self, u):
        for v in self.edges[u]:
            self.edges[v].remove(u)
        del self.edges[u]

    def get_component_size(self, u):
        q = [u]
        visited = {u}
        while q:
            current = q.pop()
            for nbr in self.edges[current]:
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)

        return len(visited)

if __name__ == '__main__':
    lines = utils.aoc_read("fs.txt")

    g = Graph(defaultdict(set))
    for l in lines:
        k = l.split(': ')[0]
        for v in [x.strip() for x in l.split(': ')[1].split(' ')]:
            g.add_edge(k,v)

    n = len(g.edges)
    # these bridge edges were found by eye by visualising with graphviz
    g.visualise()   
    g.remove_edge('gqr', 'vbk')
    g.remove_edge('klj', 'scr')
    g.remove_edge('mxv', 'sdv')

    k = g.get_component_size('psj')
    print('Part 1:', k * (n-k))