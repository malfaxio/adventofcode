#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re

circuit = {}

def execute(signal, node):
    global circuit

    print(node)
    res = None
    match circuit[node]['type']:
        case 'broadcaster':
            signal = signal
        case '%':
            print(node)
            if signal == 0:
                circuit[node]['state'] = circuit[node]['state']
                if state == True:
                    signal = 1
                else:
                    signal = 0
        case '&':
            print(node)
        case _:
            print('Error')
            exit -1

    for d in circuit[node]['dests']:
        execute(signal, d)

    return res

if __name__ == '__main__':
    lines = utils.aoc_read("ts.txt")

    m = re.compile(r'^([%&])?(\w+)\s->(.+)$')

    for l in lines:
        t = m.match(l)
        (typ, name, dst) = t.groups()
        if typ is None:
            typ = 'broadcaster'
        dests = [d.strip() for d in dst.split(',')]
        if typ in ('%', '&'):
            state = False
        else:
            state = None
        circuit[name] = {'type': typ, 'state': state, 'dests': dests}
    
    print(circuit)
    
    