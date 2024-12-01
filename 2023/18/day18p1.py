#!/usr/bin/env python3

import sys

sys.path.append('../../libs')

import utils
import re
from collections.abc import Iterable, Sequence
from itertools import pairwise


dig = []
x_min = x_max = y_min = y_max = 0

def shoelace(points: Sequence[tuple[float, float]]) -> float:
    return abs(sum((x1 * y2) - (y1 * x2) for (x1, y1), (x2, y2) in pairwise(tuple(points) + (points[0],)))) / 2

if __name__ == '__main__':
    lines = utils.aoc_read("fs.txt")

    m = re.compile('([RLUD])\s+(\d+)\s+\((.+)\)')
    x = y = 0
    points: list[tuple[int, int]] = []
    perimeter = 0
    for l in lines:
        dir, step, color = m.match(l).groups()
        step = int(step)
        match dir:
            case 'R':
                x += step
            case 'L':
                x -= step
            case 'U':
                y -= step
            case 'D':
                y += step
            case _:
                pass
                
        points.append([x,y])
        perimeter += step

    s = int(shoelace(points)) + perimeter // 2 + 1

    print(s)

    # 45809.0 too low