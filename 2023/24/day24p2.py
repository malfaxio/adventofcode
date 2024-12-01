#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import numpy as np
from sympy import Symbol
from sympy import solve_poly_system

if __name__ == '__main__':
    lines = utils.aoc_read("fs.txt")

    # reading bricks coords
    hailstones = []
    for l in lines:
        hailstones.append({'p': [int(x) for x in l.split('@')[0].split(',')], 'v': [int(x) for x in l.split('@')[1].split(',')]})

    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    vx = Symbol('vx')
    vy = Symbol('vy')
    vz = Symbol('vz')

    equations = []
    t_syms = []         #Part 2 uses SymPy. We set up a system of equations that describes the intersections, and solve it.

    #the secret sauce is that once you have three shards to intersect, there's only one valid line
    #so we don't have to set up a huge system of equations that would take forever to solve. Just pick the first three.
    for idx,h in enumerate(hailstones[:3]):
        #vx is the velocity of our throw, xv is the velocity of the shard we're trying to hit. Yes, this is a confusing naming convention.
        x0,y0,z0,xv,yv,zv = h['p'] + h['v']
        t = Symbol('t'+str(idx)) #remember that each intersection will have a different time, so it needs its own variable

        #(x + vx*t) is the x-coordinate of our throw, (x0 + xv*t) is the x-coordinate of the shard we're trying to hit.
        #set these equal, and subtract to get x + vx*t - x0 - xv*t = 0
        #similarly for y and z
        eqx = x + vx*t - x0 - xv*t
        eqy = y + vy*t - y0 - yv*t
        eqz = z + vz*t - z0 - zv*t

        equations.append(eqx)
        equations.append(eqy)
        equations.append(eqz)
        t_syms.append(t)

    #To my great shame, I don't really know how this works under the hood.
    result = solve_poly_system(equations,*([x,y,z,vx,vy,vz]+t_syms))
    print(result[0][0]+result[0][1]+result[0][2]) #part 2 answer