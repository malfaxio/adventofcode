#!/usr/bin/env python3

import sys
import re

class Board:
    def __init__(self, b):
        self.board = b.copy()
        self.beans = []
        for i in range(5):
            t = [0,0,0,0,0]
            self.beans.append(t)
    
    def print(self):
        for i in range(5):
            for j in range(5):
                if(self.beans[i][j] == 1):
                    c = "*"
                else:
                    c = " "
                print(" %2s%s" % (self.board[i][j], c), end="")
            print()
        print()
    
    def set(self, s):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == s:
                    self.beans[i][j] = 1
    
    def check(self):
        # check for row
        for i in range(5):
            w = 0
            ws = []
            for j in range(5):
                if self.beans[i][j] == 1:
                    w = w + 1
                    ws.append(self.board[i][j])
            
            if w == 5:
                break

        if w != 5:
            #check for column
            for j in range(5):
                w = 0
                ws = []
                for i in range(5):
                    if self.beans[i][j] == 1:
                        w = w + 1
                        ws.append(self.board[i][j])

                if w == 5:
                    break
        
        if w == 5:
            return ws
        else:
            return []

    def unmarkedSum(self):
        s = 0
        for i in range(5):
            for j in range(5):
                if self.beans[i][j] == 0:
                    s = s + int(self.board[i][j])
        
        return s



if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    f = open(sys.argv[1])
    lines = f.readlines()

    extractions = lines[0].split(",")

    p = re.compile("\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)")

    i = 0
    boards = []
    ib = 0
    b = []
    for l in lines:
        if i >= 2:
            if l != "\n":
                m = p.match(l) 
                b.append([m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)])
            else:
                tb = Board(b)
                boards.append(tb)
                b = []
        i = i + 1
    tb = Board(b)
    boards.append(tb)

    for n in extractions:
        print("Drawn: %s" %n)
        for b in boards:
            b.set(n)
            b.print()
            r = b.check()
        
            if len(r) > 0:
                nw = int(n)
                break
        
        if len(r) > 0:
            break
    
    s1 = b.unmarkedSum()

    print("Unmarked: %d  Marked: %d  Result: %d" % (s1, nw, s1*nw))