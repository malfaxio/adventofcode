#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    f = open(sys.argv[1])
    lines = f.readlines()

    first = True
    inc = 0
    deep_old = 0
    for l in lines:
        deep = int(l)

        if first == False:
            if deep > deep_old:
                inc = inc + 1

        if first == True:
            first = False
                    
        deep_old = deep

    
    print("Increments: %d \n" % inc)
        
