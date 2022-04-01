#!/usr/bin/env python3

import re
import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()
    
    p = re.compile("([A-Z]+)\s->\s([A-Z])")

    template = lines[0]
    rules = []
    for l in lines[2:]:
        g = p.match(l)
        rules.append([g.group(1), g.group(2)])

    
    for iter in range(10):
        print(iter)
        c = ""
        polymer = ""
        for t in template:
            c += t
            if len(c) == 2:
                for r in rules:
                    if r[0] == c:
                        break
                
                polymer += c[0] + r[1]
                c = t
        polymer += r[0][1]
        template = polymer

    counters = {}
    for c in polymer:
        if c in counters:
            counters[c] += 1
        else:
            counters[c] = 1

    values = [ v for k, v in sorted(counters.items(), key=lambda item: item[1]) ]

    print("Results %d - %d = %d" % (values[-1], values[0], values[-1]-values[0]))