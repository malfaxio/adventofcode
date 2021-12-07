#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    f = open(sys.argv[1])
    lines = f.readlines()

    gamma = epsilon = ""

    for i in range(len(lines[0])-1):
        print("i: %d" % i)
        b0 = b1 = 0
        for l in lines:
            if l[i] == "0":
                b0 = b0 + 1
            else:
                b1 = b1 + 1

        if b0 > b1:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        else:
            gamma = gamma + "1"
            epsilon = epsilon + "0"

    print("Gamma  : %s\nEpsilon: %s" % (gamma, epsilon))
    print("Gamma  : %d\nEpsilon: %d\nResult1: %d" % (int(gamma,2), int(epsilon,2), int(gamma,2)*int(epsilon,2)))