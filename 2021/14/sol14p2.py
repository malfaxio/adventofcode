#!/usr/bin/env python3

import sys

def enrich(t):
    res = ""
    i = 0
    while i < len(t)-1:
        if t[i]+t[i+1] in pairins:
            res += t[i] + pairins[t[i]+t[i+1]]

        i += 1
    res += t[i]

    return res

def findMinMax(t):
    stat = {}
    for c in t:
        if c in stat:
            stat[c] += 1
        else:
            stat[c] = 1

    f = True
    for k in stat:
        s = stat[k]
        if f:
            mi = s
            ma = s
            f = False
        else:
            if s < mi:
                mi = s
            if s > ma:
                ma = s
        

    return (mi, ma)


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    iteractions = 40
    pairins = {}
    template = {}
    i = 0
    for l in open(sys.argv[1]).read().splitlines():
        if i == 0:
            for x, y in zip(l, l[1:]):
                if x+y not in template:
                    template[x+y] = 0
                template[x+y] += 1
        elif i > 1:
            (r1, r2) = l.split(" -> ")
            pairins[r1] = r2
        i += 1

    for i in range(iteractions):
        temp = {}
        for t in template:
            q = pairins[t]
            if t[0]+q not in temp:
                temp[t[0]+q] = 0
            temp[t[0]+q] += template[t]
            if q+t[1] not in temp:
                temp[q+t[1]] = 0
            temp[q+t[1]] += template[t]
        template = temp

    r1 = {}
    r2 = {}
    for t in template:
        if t[0] not in r1:
            r1[t[0]] = 0
        r1[t[0]] += template[t]
        if t[1] not in r2:
            r2[t[1]] = 0
        r2[t[1]] += template[t]
        

    r = {x: max(r1.get(x, 0), r2.get(x, 0)) for x in set(r1) | set(r2)}

    print(max(r.values()) - min(r.values()))
