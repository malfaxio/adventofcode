#!/usr/bin/env python3

import json
import os

with open('aoc_stats.json', 'r') as openfile:
    # Reading from json file
    aoc = json.load(openfile)
    openfile.close()

if os.path.isfile('last_ts.txt'):
    with open('last_ts.txt', 'r') as ts:
        last_ts = int(ts.read())
        ts.close()
else:
    last_ts = 0

star = [ 'x', 'silver', 'gold' ]

events = {}
f = True
for u in aoc['members'].values():
    f = False
    for (pn, s) in u['completion_day_level'].items():
        for (d1, p) in s.items():
            #print(f"{p['get_star_ts']} user X problem {pn} get {star[int(d1)]} ")
            if p['get_star_ts'] > last_ts:
                events[p['get_star_ts']] = f"user: \'{u['name']}\' problem {pn} get {star[int(d1)]} "

if len(events.keys()) > 0:
    for (t, e) in sorted(events.items()):
        print(f"{t} {e}")

    with open('last_ts.txt', 'w') as ts:
        ts.write(str(t))
        ts.close()