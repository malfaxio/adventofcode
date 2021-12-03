#!/usr/bin/env python3

import sys
import string


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    f = open(sys.argv[1])
    lines = f.readlines()

    mostcommon = lesscommon = ""
    oxygen_o = co2scrubber_o = lines.copy()
    for i in range(len(lines[0])-1):
        b0 = b1 = 0
        for l in oxygen_o:
            if l[i] == "0":
                b0 = b0 + 1
            else:
                b1 = b1 + 1

        if b1 >= b0:
            mostcommon = "1"
        else:
            mostcommon = "0"
        
        oxygen = []
        if len(oxygen_o) > 1:
            for l in oxygen_o:
                if l[i] == mostcommon:
                    oxygen.append(l)
            
            oxygen_o = oxygen.copy()

        b0 = b1 = 0
        for l in co2scrubber_o:
            if l[i] == "0":
                b0 = b0 + 1
            else:
                b1 = b1 + 1
        if b0 <= b1:
            lesscommon = "0"
        else:
            lesscommon = "1"
        
        co2scrubber = []
        if len(co2scrubber_o) > 1:
            for l in co2scrubber_o:
                if l[i] == lesscommon:
                    co2scrubber.append(l)

            co2scrubber_o = co2scrubber.copy()

        print(oxygen_o)
        print(co2scrubber_o)
    
    print("Oxygen rating: %d\nCO2 scrubber : %d\nResult 2     : %d" %(int(oxygen_o[0],2), int(co2scrubber_o[0],2), int(oxygen_o[0],2)*int(co2scrubber_o[0],2)))