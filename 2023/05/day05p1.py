#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re

lines = utils.aoc_read_bysection("fs.txt")

seeds = [int(x) for x in lines[0][0].split(" ")[1:]]

def get(x, lst):
    r = x
    for l in lst:
        if l[1] <= x <= (l[1] + l[2] - 1):
            r = l[0]+(x-l[1])
            break

    return r

for l in lines[1:]:
    if l[0] == 'seed-to-soil map:':
        seed2soil = []
        for m in l[1:]:
            seed2soil.append([int(x) for x in m.split(" ")])
    elif l[0] == 'soil-to-fertilizer map:':
        soil2fertilizer = []
        for m in l[1:]:
            soil2fertilizer.append([int(x) for x in m.split(" ")])
    elif l[0] == 'fertilizer-to-water map:':
        fertilizer2water = []
        for m in l[1:]:
            fertilizer2water.append([int(x) for x in m.split(" ")])
    elif l[0] == 'water-to-light map:':
        water2light = []
        for m in l[1:]:
            water2light.append([int(x) for x in m.split(" ")])
    elif l[0] == 'light-to-temperature map:':
        light2temperature = []
        for m in l[1:]:
            light2temperature.append([int(x) for x in m.split(" ")])
    elif l[0] == 'temperature-to-humidity map:':
        temperature2humidity = []
        for m in l[1:]:
            temperature2humidity.append([int(x) for x in m.split(" ")])
    elif l[0] == 'humidity-to-location map:':
        humidity2location = []
        for m in l[1:]:
            humidity2location.append([int(x) for x in m.split(" ")])

locations = []
for seed in seeds:
    soil = get(seed, seed2soil)
    fertilizer = get(soil, soil2fertilizer)
    water = get(fertilizer, fertilizer2water)
    light = get(water, water2light)
    temp = get(light, light2temperature)
    hum = get(temp, temperature2humidity)
    loc = get(hum, humidity2location)
    locations.append(loc)

print(min(locations))