#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    f = open(sys.argv[1])
    lines = f.readlines()

    inc = 0
    
    triplet_old = int(lines[0])+int(lines[1])+int(lines[2])
    for i in range(3,len(lines)):
        triplet = int(lines[i-2])+int(lines[i-1])+int(lines[i])
        
        if triplet > triplet_old:
            inc = inc + 1

        triplet_old = triplet

    print("Increments: %d \n" % inc)
