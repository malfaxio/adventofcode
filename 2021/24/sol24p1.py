#!/usr/bin/env python3

from math import trunc
import sys   

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    valids = 0
    #modelnumber = 99999999999999
    #modelnumber = 99999987473000
    #modelnumber = 99999958454000
    modelnumber = 99995731700000

    while modelnumber > 0:
        
        if str(modelnumber).find("0") < 0:
            stack = [int(a) for a in str(modelnumber)]
            stack.reverse()
            vars = {"w": 0, "x": 0, "y": 0, "z": 0}
            for line in lines:
                s = line.split(" ")
                op = s[0]
                args = s[1:]

                if op == "inp":
                    vars[args[0]] = stack.pop()
                elif op == "add":
                    if args[1] not in vars:
                        v = int(args[1])
                    else:
                        v = vars[args[1]]
                    vars[args[0]] += v
                elif op == "mul":
                    if args[1] not in vars:
                        v = int(args[1])
                    else:
                        v = vars[args[1]]
                    vars[args[0]] *= v
                elif op == "div":
                    if args[1] not in vars:
                        v = int(args[1])
                    else:
                        v = vars[args[1]]
                    vars[args[0]] = trunc(vars[args[0]] / v)
                elif op == "mod":
                    if args[1] not in vars:
                        v = int(args[1])
                    else:
                        v = vars[args[1]]
                    vars[args[0]] %= v
                elif op == "eql":
                    if args[1] not in vars:
                        v = int(args[1])
                    else:
                        v = vars[args[1]]
                    if vars[args[0]] == v:
                        vars[args[0]] = 1
                    else:
                        vars[args[0]] = 0

            if vars["z"] == 0:
                # model is valid
                print("Valid %s" % modelnumber)
                print(vars)
                break

        else:
            if modelnumber % 100000 == 0: print(modelnumber)

        modelnumber -= 1


    print("Valid: %d" % modelnumber)