#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
from heapq import heappush, heappop

def tadd(a,b): return (a[0]+b[0],a[1]+b[1])

def solve(mi,ma):
    heap = [(0,(0,0),(0,0))]
    visited = {((0,0),(0,0))}
    while len(heap):
        cost, pos, lsdir = heappop(heap)
        for di in range(-1,2):
            if di == 0:
                if lsdir[1] == ma: continue
                else: idx = lsdir[1]+1
            else:
                idx = 1
                if 0< lsdir[1] < mi: continue
            ndi = (lsdir[0]+di)%4
            npos = tadd(pos, dirs[ndi])
            if (npos in sparse) and ((npos,(ndi,idx)) not in visited):
                ncost = cost + sparse[npos]
                if npos == (n-1,m-1): return ncost
                visited.add((npos,(ndi,idx)))
                heappush(heap,(ncost,npos,(ndi,idx)))

if __name__ == '__main__':
    map = utils.aoc_read("fs.txt")

    sparse = {(i,j):int(c) for i,line in enumerate(map) for j,c in enumerate(line)}
    n,m = len(map), len(map[0])
    dirs = [(1,0), (0,-1), (-1,0), (0,1)]
    
    print("Part1: %d Part2: %d" % (solve(0,3),solve(4,10)))