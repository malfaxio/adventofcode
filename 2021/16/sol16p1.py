#!/usr/bin/env python3

import sys

def header(sig):
    ver = int(sig[0:3],2)
    typ = int(sig[3:6],2)

    return ver, typ

def parse(sig):
    if len(sig) <= 6:
        return len(sig), [0]
        
    print("Sig: %s " % sig)
    ver = []
    v, typ = header(sig[0:6])

    ver.append(v)
    print("V: %d T: %d" % (v, typ))
    b = 6
    if typ == 4:
        # Literal
        cont = "1"
        lit = ""
        while cont == "1":
            cont = sig[b:b+1]
            lit += sig[b+1:b+5]
            b += 5
            #print("Cont: %s lit: %s" % (cont, lit))
        print("Literal: %d" % int(lit,2))
    else:
        lt = sig[b]
        b += 1
        if lt == "0":
            print("First: %s" % sig[b:b+15])
            try:
                l = int(sig[b:b+15],2)
            except ValueError:
                l = 0
            b += 15
            print("Lenght: %d" % l)
            while b < l:
                db, v = parse(sig[b:b+l])
                b += db
                for x in v:
                    ver.append(x)

        elif lt == "1":
            n = int(signal[b:b+11],2)
            b += 11
            for i in range(n):
                t, v = parse(sig[b:])
                for x in v:
                    ver.append(x)
                b += t

    return b, ver

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    signal = ""
    for c in lines[0]:
        t = "{:04b}".format(int(c,base=16))
        signal += t

    b = 0
    versions = []
    #try:
    while b < len(signal):
        db, v = parse(signal[b:])
        for x in v:
            versions.append(x)
        b += db
    #except ValueError:
    #    print("Remains: %s" % signal[b:])
    
    print("Results: %d " % sum(versions))