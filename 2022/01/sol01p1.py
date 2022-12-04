#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines() 

    elf_max = 0
    t = 0
    for l in lines:
        if l != "":
            t += int(l)
        else:
            if t > elf_max:
                elf_max = t
            t = 0
    if t > elf_max:
        elf_max = t

    print("Total Cals carried: %d" % elf_max)