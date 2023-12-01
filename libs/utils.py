
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