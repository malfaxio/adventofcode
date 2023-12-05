#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re
import multiprocessing

seed2soil = []
soil2fertilizer = []
fertilizer2water = []
water2light = []
light2temperature = []
temperature2humidity = []
humidity2location = []


def get(x, lst):
    r = x
    for l in lst:
        if l[1] <= x <= (l[1] + l[2] - 1):
            r = l[0]+(x-l[1])
            break

    return r

def init_worker(s2s, s2f, f2w, w2l, l2t, t2h, h2l):
    # declare scope of a new global variable
    global seed2soil
    global soil2fertilizer
    global fertilizer2water
    global water2light
    global light2temperature
    global temperature2humidity
    global humidity2location
    # store argument in the global variable for this process
    seed2soil = s2s
    soil2fertilizer = s2f
    fertilizer2water = f2w
    water2light = w2l
    light2temperature = l2t 
    temperature2humidity = t2h
    humidity2location = h2l

def task(r):
    global seed2soil
    global soil2fertilizer
    global fertilizer2water
    global water2light
    global light2temperature
    global temperature2humidity
    global humidity2location


    location = float('inf')
    for seed in range(r[0], r[0] + r[1]):
        soil = get(seed, seed2soil)
        fertilizer = get(soil, soil2fertilizer)
        water = get(fertilizer, fertilizer2water)
        light = get(water, water2light)
        temp = get(light, light2temperature)
        hum = get(temp, temperature2humidity)
        loc = get(hum, humidity2location)
        if loc < location:
            location = loc

    return location


if __name__ == '__main__':
    lines = utils.aoc_read_bysection("fs.txt")

    seeds_t = [int(x) for x in lines[0][0].split(" ")[1:]]
    f = True
    seeds = []
    t = []
    for s in seeds_t:
        t.append(s)
        if f:
            f = False
        else:
            f = True
            seeds.append(t)
            t =  []
    
    for l in lines[1:]:
        if l[0] == 'seed-to-soil map:':
            for m in l[1:]:
                seed2soil.append([int(x) for x in m.split(" ")])
        elif l[0] == 'soil-to-fertilizer map:':
            for m in l[1:]:
                soil2fertilizer.append([int(x) for x in m.split(" ")])
        elif l[0] == 'fertilizer-to-water map:':
            for m in l[1:]:
                fertilizer2water.append([int(x) for x in m.split(" ")])
        elif l[0] == 'water-to-light map:':
            for m in l[1:]:
                water2light.append([int(x) for x in m.split(" ")])
        elif l[0] == 'light-to-temperature map:':
            for m in l[1:]:
                light2temperature.append([int(x) for x in m.split(" ")])
        elif l[0] == 'temperature-to-humidity map:':
            for m in l[1:]:
                temperature2humidity.append([int(x) for x in m.split(" ")])
        elif l[0] == 'humidity-to-location map:':
            for m in l[1:]:
                humidity2location.append([int(x) for x in m.split(" ")])

    with multiprocessing.Pool(initializer=init_worker, initargs=(seed2soil, soil2fertilizer, fertilizer2water, water2light, light2temperature, temperature2humidity, humidity2location)) as pool:
        # call the function for each item in parallel
        locs = []
        for loc in pool.map(task, seeds):
            print(loc)
            locs.append(loc)

        pool.close()

    print(min(locs))