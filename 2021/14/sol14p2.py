#!/usr/bin/env python3

<<<<<<< HEAD
=======
import re
>>>>>>> 592ad0d5d3150f85712c98ee36d2530362fb619a
import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

<<<<<<< HEAD
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
=======
    lines = open(sys.argv[1]).read().splitlines()
    
    p = re.compile("([A-Z]+)\s->\s([A-Z])")

    template = lines[0]
    rules = {}
    for l in lines[2:]:
        g = p.match(l)
        rules[g.group(1)] = g.group(1)[0]+g.group(2)

    print(rules)
    
    for iter in range(40):
        print(iter)
        c = ""
        polymer = ""
        for t in template:
            c += t
            if len(c) == 2:
                for r,v in rules.items():
                    if r == c:
                        break
                
                polymer += v
                c = t
        polymer += t
        template = polymer

    counters = {}
    for c in polymer:
        if c in counters:
            counters[c] += 1
        else:
            counters[c] = 1

    values = [ v for k, v in sorted(counters.items(), key=lambda item: item[1]) ]

    print("Results %d - %d = %d" % (values[-1], values[0], values[-1]-values[0]))
>>>>>>> 592ad0d5d3150f85712c98ee36d2530362fb619a
