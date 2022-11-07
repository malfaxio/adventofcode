#!/usr/bin/env python3

import sys
import re

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    signals = {}
    beacons = []
    for l in lines:
        if l[0:2] == "--":
            print(beacons)
            if len(beacons) > 0:
                signals[scannerid] = beacons

            beacons = []
            # new scanner
            p = re.compile("--- scanner (\d+) ---")
            m = p.match(lines[0])
            scannerid = m[0]

        b = re.search("([-\d]+),([-\d]+),([-\d]+)", l)
        if b:
            beacons.append([b.group(1), b.group(2), b.group(3)])



