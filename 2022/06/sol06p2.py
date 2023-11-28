#!/usr/bin/env python3

import re
import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    for l in lines:
        print(l)
        s = []
        for i in range(len(l)):
            if l[i] not in s:
                s.append(l[i])
            else:
                s = s[s.index(l[i])+1:]
                s.append(l[i])
            if len(s) == 14:
                break
        print(i+1)
