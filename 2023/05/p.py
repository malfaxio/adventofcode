#!/usr/bin/env python3

ranges = [ [1187290020, 247767461], [ 40283135, 64738286] ]

def split_range(r, cs):
  res = []
  for i in range(r[0], r[1], cs):
    f = i+cs-1
    if i+cs >= r[1]:
      f = r[1]
    res.append((i, f))
    print(i, f)

  return res

for r in ranges:
  s = split_range((r[0], r[0]+r[1]), 10000000)
  print(s)
