#!/usr/bin/env python3

import re
import sys


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    monkeys = []
    items = []
    operation = []
    operand = []
    truetarget = []
    falsetarget = []
    divtest = []
    insp = []
    m = re.compile("Monkey (\d+):\s+Starting items: ([\s,\d]+)\s\sOperation: new = old (\*|\+) (\d+|old)\s+Test: divisible by (\d+)\s+If true: throw to monkey (\d+)\s+If false: throw to monkey (\d+)")
    data = ""
    tdivtest = 1
    for l in lines:
        if l != "":
            data += l
        else:
            (id, it, o1, o2, div, tt, ft) = m.findall(data)[0]
            operand.append(o2)
            operation.append(o1)
            divtest.append(int(div))
            tdivtest *= int(div)
            truetarget.append(int(tt))
            falsetarget.append(int(ft))
            for i in it.split(','):
                items.append(int(i.strip()))
                monkeys.append(int(id))
            insp.append(0)
            data = ""
    (id, it, o1, o2, div, tt, ft) = m.findall(data)[0]
    operand.append(o2)
    operation.append(o1)
    divtest.append(int(div))
    tdivtest *= int(div)
    truetarget.append(int(tt))
    falsetarget.append(int(ft))
    insp.append(0)
    for i in it.split(','):
        items.append(int(i.strip()))
        monkeys.append(int(id))

    for r in range(10000):
        print(r)
        for id in range(len(operand)):
            for i in [index for (index, item) in enumerate(monkeys) if item == id]:
                insp[id] += 1
                if operand[id] == 'old':
                    o = items[i]
                else:
                    o = int(operand[id])
                if operation[id] == '*':
                    items[i] *= o
                elif operation[id] == '+':
                    items[i] += o
                
                # Relief
                # items[i] = int(items[i] / 3)
                items[i] %= tdivtest
                
                if (items[i] % divtest[id]) == 0:
                    monkeys[i] = truetarget[id]
                else:
                    monkeys[i] = falsetarget[id]

    insp.sort()
    print(insp[-1] * insp[-2])