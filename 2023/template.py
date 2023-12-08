#!/usr/bin/env python3

import sys

sys.path.append('../libs')

import utils


if __name__ == '__main__':
    l = utils.aoc_read_bysection("test.txt", convert="int")

    print(l)