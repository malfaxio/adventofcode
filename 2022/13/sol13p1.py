#!/usr/bin/env python3

import json
import sys

def compare(left, right):
    r = True
    i = 0
    while r and (i < len(left) or (i < len(right))):
        print(" - %s == %s" % (str(left[i]), str(right[i])))
        if type(left[i]) == int and type(right[i]) == int:
            if left[i] > right[i]:
                r = False
        elif type(left[i]) != int and type(right[i]) != int:
            r = compare(left[i], right[i])
        elif type(left[i]) != int and type(right[i]) == int:
            r = compare(left[i], [right[i]])
            
        i += 1

    return r
    

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    c = 0
    signals = [ [], [] ]
    for l in lines[0:5]:
        if "[" in l:
            signals[c] = eval(l)
            if c == 1:
                print("Compare: %s vs %s" % (str(signals[0]), str(signals[1]) ) ) 
                good = compare(signals[0], signals[1])

                if good:
                    print("Ok")
                else:
                    print("Not OK")
            c += 1
        else:
            c = 0