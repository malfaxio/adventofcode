#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()
    
    p = re.compile("([A-Z]+)\s->\s([A-Z])")

 