#!/usr/bin/env python3

import sys

def header(sig):
    ver = int(sig[0:3],2)
    typ = int(sig[3:6],2)

    return ver, typ

def parse(sig, indent = 0):
    vers = []
    vals = []
    b = 0
    val = 0
    if len(sig) > 6:
        valid = True
        v, t = header(sig[b:b+6]); b+= 6
        print("".rjust(indent) + "Vers: %d TypeID: %d" % (v,t))
        vers.append(v)
        if t == 4 and b < len(sig):
            cont = "1"
            lit = ""
            while cont == "1":
                cont = sig[b]; b += 1
                lit += sig[b:b+4]; b += 4
            val = int(lit, 2)
            print("".rjust(indent) + str(val))

        elif t != 4 and b < len(sig):
            ltid = sig[b]; b+= 1
            if ltid == "0" and len(sig[b:]) > 15:
                l = int(sig[b:b+15], 2); b += 15
                l += b
                while b < l:
                    db, v, val = parse(sig[b:], indent+2)
                    for x in v:
                        vers.append(x)
                    vals.append(val)
                    b += db
            elif ltid == "1" and len(sig[b:]) > 11:
                n = int(sig[b:b+11], 2); b += 11
                while n > 0:
                    db, v, val = parse(sig[b:], indent+2)
                    for x in v:
                        vers.append(x)
                    vals.append(val)
                    n -= 1
                    b += db
            else:
                valid = False

            if valid:
                if t == 0:
                    # +
                    val = sum(vals)
                    print("".rjust(indent) + "sum(%s) = %d" % (vals, val))
                elif t == 1:
                    val = vals[0]
                    for x in vals[1:]:
                        val *= x
                    print("mul(%s) = %d" % (vals, val))
                elif t == 2:
                    val = min(vals)
                    print("".rjust(indent) + "min(%s) = %d" % (vals, val))
                elif t == 3:
                    # max
                    val = max(vals)
                    print("".rjust(indent) + "max(%s) = %d" % (vals, val))
                elif t == 5:
                    # >
                    val = 0
                    if vals[0] > vals[1]:
                        val = 1
                    print("".rjust(indent) + "%d > %d: %d" % (vals[0], vals[1], val))
                elif t == 6:
                    # <
                    val = 0
                    if vals[0] < vals[1]:
                        val = 1
                    print("".rjust(indent) + "%d < %d: %d" % (vals[0], vals[1], val))
                elif t == 7:
                    # ==
                    val = 0
                    if vals[0] == vals[1]:
                        val = 1
                    print("".rjust(indent) + "%d == %d: %d" % (vals[0], vals[1], val))

    else:
        b = len(sig)

    return b, vers, val

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    for line in lines:
        print(line)
        signal = ""
        for c in line:
            t = "{:04b}".format(int(c, base=16))
            signal += t

        b = 0
        versions = []
        values = []
        
        while b < len(signal):
            print(signal[b:])
            db, ver, val = parse(signal[b:])
            b += db
            for x in ver:
                versions.append(x)
            if db > 6:
                values.append(val)

        print("Ver sum: %d" % sum(versions))
        print("Value: %s" % values)
