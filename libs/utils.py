
def aoc_read(filename):
    try:
        print("Opening: %s" % filename)
        with open(filename) as f:
            lines = f.read().splitlines() 

        return lines
    except Exception as e:
        print(e)
        exit(-1)

    return []

def aoc_read_bysection(filename, convert="no"):
    lines = aoc_read(filename)

    r = []
    p = []
    for l in lines:
        if l == '':
            r.append(p)
            p = []
        else:
            if convert == "int":
                p.append(int(l))
            else:
                p.append(l)
    r.append(p)

    return r

def rechunk(r, cs):
    res = []
    for i in range(r[0], r[1], cs):
        f = i+cs-1
        if i+cs >= r[1]:
            f = r[1]
        res.append((i, f))

    return res