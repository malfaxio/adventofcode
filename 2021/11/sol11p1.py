#!/usr/bin/env python3

import sys

def increaseEnergies():
    global energies

    for y in range(len(energies)):
        for x in range(len(energies[y])):
            energies[y][x] += 1


def Flashes():
    global energies
    
    c = 0
    for y in range(len(energies)):
        for x in range(len(energies[y])):
            if energies[y][x] > 9:
                energies[y][x] = 0
                increaseAdjacent(x,y)
                c += 1

    if c > 0:
        return True
    else:
        return False


def increaseAdjacent(sx, sy):
    global energies

    mx = len(energies[0])
    my = len(energies)
    for y in range(sy-1, sy+2):
        for x in range(sx-1, sx+2):
            if x >= 0 and x < mx and y >= 0 and y < my and not (sx == x and sy == y):
                if energies[y][x] > 0:
                    energies[y][x] += 1


def countFlashes():
    global energies

    c = 0
    for y in range(len(energies)):
        for x in range(len(energies[y])):
            if energies[y][x] == 0:
                c += 1

    return c


def printEnergies():
    global energies

    for y in range(len(energies)):
        for x in range(len(energies[y])):
            c = energies[y][x]
            if c > 9:
                c = 0
            print(c,end="")
        print()

if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    energies = []
    for l in lines:
        energies.append([int(x) for x in l])

    flashes = 0
    for i in range(100):
        # Increase Energy by 1
        increaseEnergies()

        # Increase neighborhood
        r = True
        while r:
            r = Flashes()

        # Count flashes
        flashes += countFlashes()

    print("Flashes: %d" % flashes)
