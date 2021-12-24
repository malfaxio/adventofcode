#!/usr/bin/env python3

import sys
import re

def hitCheck(x, y):
    global target_x1, target_x2, target_y2, target_y1

    r = False
    if x >= target_x1 and x <= target_x2:
        if y >= target_y2 and y <= target_y1:
            r = True

    return r

def simulate(vx, vy):
    global target_x2, target_y2
    print("Vel X: %d  Vel Y: %d" % (vx, vy))

    step = 0
    x = y = maxy = 0
    while True:
        x += vx
        y += vy
        if y > maxy: maxy = y
        if vx > 0: vx -= 1
        if vx < 0: vx += 1
        vy -= 1
        print("Step: %d  (%d,%d) vx: %d vy: %d" % (step, x, y, vx, vy))
        if hitCheck(x,y):
            print("Hit!")
            hit = True
            break
        if x > target_x2 or y < target_y2:
            hit = False
            break

        step += 1

    return hit, maxy


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])

    lines = open(sys.argv[1]).read().splitlines()

    p = re.compile("target area: x=(\d+)\.\.(\d+), y=([-]*\d+)\.\.([-]*\d+)")
    m = p.match(lines[0])
    target_x1 = int(m.group(1))
    target_x2 = int(m.group(2))
    target_y2 = int(m.group(3))
    target_y1 = int(m.group(4))

    print("Target: %d,%d -> %d,%d" %(target_x1,target_y1, target_x2, target_y2))

    heights = []
    hitCounter = 0
    for vx in range(1,100):
        for vy in range(-200,200):
            hit, h = simulate(vx, vy)
            if hit:
                hitCounter += 1
                heights.append(h)

    print(max(heights))
    print(hitCounter)