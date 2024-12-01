#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re

if __name__ == '__main__':
    flows = {}
    (workflows, ratings) = utils.aoc_read_bysection("tss.txt")

    re_w = re.compile(r'(\w+){(.+)}')
    re_r = re.compile(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')
    re_ru = re.compile(r'(.)([<>])(\d+)\:(\w+)')
    for w in workflows:
        m_w = re_w.match(w)
        flows[m_w.group(1)] = m_w.group(2).split(',')

    print(flows)
    ratings = []
    for x in range(1,4001):
        for m in range(1,4001):
            for a in range(1,4001):
                for x in range(1,4001):
                    ratings.append([x,m,a,x])

    exit

    res = 0
    for rat in ratings:
        m_rat = re_r.match(rat)
        reg = {}
        (reg['x'], reg['m'], reg['a'], reg['s']) = [int(x) for x in m_rat.groups()]
        print(reg)
        w = 'in'
        while(True):
            print(w)
            fr = None
            if w not in ('A','R'):
                for ru in flows[w]:
                    m_ru = re_ru.match(ru)
                    if m_ru is not None:
                        (r, o, v, l) = m_ru.groups()
                        v = int(v)
                        match o:
                            case '>':
                                if reg[r] > v:
                                    w = l
                                    break
                            case '<':
                                if reg[r] < v:
                                    w = l
                                    break
                    else:
                        if ru in ('A', 'R'):
                            w = ru
                            break
                        else:
                            w = ru
                            break
            else:
                break

        if w == 'A':
            s = (reg['x'] + reg['m'] + reg['a'] + reg['s'])
            print(f'A {reg} = {s}')
            res += s

    print(res)