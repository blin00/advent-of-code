from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day13.py < sample.in
echo "=== real ===" ; py day13.py < day13.in
echo "=== sample ===" ; py day13.py < sample.in ; echo "=== real ===" ; py day13.py < day13.in
"""

# A = read_input('/dev/stdin')

f = open('/dev/stdin')
parts = f.read().strip().split('\n\n')
assert len(parts) == 2

A = parts[0].strip().splitlines()
inst = parts[1].strip().splitlines()

grid = defaultdict(int)

for line in A:
    x, y = map(int, line.split(','))
    grid[(x, y)] = 1


for line in inst:
    _, _, p = line.split(' ')
    what, coord = p.split('=')
    coord = int(coord)
    to_yeet = []
    to_add = []
    if what == 'x':
        for k, v in list(grid.items()):
            if not v:
                continue
            x, y = k
            assert x != coord
            if x < coord:
                pass
            else:
                d = x - coord
                to_yeet.append((x, y))
                to_add.append((coord - d, y))
                assert coord - d >= 0
    else:
        for k, v in list(grid.items()):
            if not v:
                continue
            x, y = k
            assert y != coord
            if y < coord:
                pass
            else:
                d = y - coord
                to_yeet.append((x, y))
                to_add.append((x, coord - d))
                assert coord - d >= 0
    for x, y in to_yeet:
        del grid[(x, y)]
    for x, y in to_add:
        grid[(x, y)] = 1
    res = 0

    for k, v in grid.items():
        if v:
            res += 1

    print(res)
dump_dict_grid(grid, lambda t: '#' if t else '.')
