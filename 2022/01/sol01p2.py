#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines() 

    elf_max = []
    t = 0
    for l in lines:
        if l != "":
            t += int(l)
        else:
            elf_max.append(t)
            t = 0
    elf_max.append(t)
    elf_max.sort(reverse = True)
    print(elf_max[0:3])

    s = 0
    for t in elf_max[0:3]:
        print(t)
        s += t


    print("Total Cals carried: %d" % s)