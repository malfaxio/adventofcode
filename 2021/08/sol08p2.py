#!/usr/bin/env python3

import sys

class Digit:
    def __init__(self, flag):
        self.signal = ""
        self.translator = {}
        self.invert1 = False
        self.invert4 = False
        if flag[0] == "1":
            self.invert1 = True
        if flag[1] == "1":
            self.invert4 = True


    def setSignal(self, s):
        self.signal = s

    def getValue(self):
        values = { "abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9 }
        
        return values[self.translate(self.signal)]

    def set1(self, s):
        if self.invert1:
            c1 = "fc"
        else:
            c1 = "cf"
        self.translator[s[0]] = c1[0]
        self.translator[s[1]] = c1[1]

    def set4(self, s):
        if self.invert4:
            c4 = "db"
        else:
            c4 = "bd"
        i = 0
        for c in s:
            if c not in self.translator:
                self.translator[c] = c4[i]
                i += 1

    def set7(self, s):
        for c in s:
            if c not in self.translator:
                self.translator[c] = "a"

    def guess(self, s):
        tr = self.translate(s)
        #print("%s -> %s" % (s, tr), end="")
        values = { "abdf": "g", "acdf": "g", "abcdf": "g", "acdg": "e", "abdfg": "e", "abcfg": "e" }
        if len(tr) == len(s)-1:
            for c in s:
                if c not in self.translator and tr in values:
                    self.translator[c] = values[tr]
                    #print("  guessed: %s -> %s" % (c, values[tr]), end="")
        #print()

        if len(self.translator) == 6:
            for c in "abcdefg":
                if c not in self.translator:
                    if values[tr] == "g":
                        self.translator[c] = "e"
                    else:
                        self.translator[c] = "g"
            

        if len(self.translator) == 7:
            #print(self.translator)
            return True
        else:
            return False

    def translate(self, s):
        r = ""
        for c in s:
            if c in self.translator:
                r += self.translator[c]

        return "".join(sorted(r))

    def getTranslator(self):
        return self.translator


if len(sys.argv) == 2:
    print("Opening: %s" % sys.argv[1])
    f = open(sys.argv[1])
    lines = f.readlines()

    values = []
    for line in lines:
        t = line.strip().split(" | ")
        signals = t[0].split(" ")
        outputs = t[1].split(" ")

        iter = True
        iflag = 0
        flag = ["00", "01", "10", "11"]
        value = ""
        while(iter):
            iter = False
            d = Digit(flag[iflag])

            for s in signals:
                if len(s) == 2:
                    s1 = s
                if len(s) == 3:
                    s7 = s
                if len(s) == 4:
                    s4 = s
            
            d.set1(s1)
            d.set4(s4)
            d.set7(s7)

            for s in signals:
                if d.guess(s):
                    break

            try:
                for o in outputs:
                    d.setSignal(o)
                    #print("Output %s translate in %s value: %d" % (o, d.translate(o), d.getValue())) 
                    value += str(d.getValue())
            except KeyError:
                iflag += 1
                value = ""
                iter = True
        values.append(int(value))
        print("Value: %s" % value)

    print("Result: %d" % sum(values))