# from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; pypy3 day14.py < sample.in
echo "=== real ===" ; pypy3 day14.py < day14.in
echo "=== sample ===" ; pypy3 day14.py < sample.in ; echo "=== real ===" ; pypy3 day14.py < day14.in
"""

A = sys.stdin.read().strip().splitlines()
# A = sys.stdin.read().strip().split('\n\n')

N = len(A)

# source is 500, 0

SIZE = int(2e3)

grid = [['.'] * SIZE for _ in range(SIZE)]

max_y = 0

for line in A:
    pts = line.split(' -> ')
    pts = [parse_coord(pt) for pt in pts]        
    max_y = max(max_y, max(pts[i][1] for i in range(len(pts))))
    for i in range(1, len(pts)):
        x0, y0 = pts[i-1]
        x1, y1 = pts[i]
        assert x0 == x1 or y0 == y1
        for x, y in rline(x0, y0, x1, y1):
            grid[y][x] = '#'
for x in range(0, SIZE):
    grid[max_y + 2][x] = '#'

def drop_sand(x, y):
    while True:
        if y > SIZE - 39:
            return None
        assert x > 0 and x < SIZE - 1        
        if grid[y + 1][x] == '.':
            y += 1
        elif grid[y + 1][x - 1] == '.':
            y += 1
            x -= 1
        elif grid[y + 1][x + 1] == '.':
            y += 1
            x += 1
        else:
            return x, y
res = 0
while True:
    r = drop_sand(500, 0)
    res += 1
    if r == (500, 0):
        print(res)
        break
    else:
        x, y = r
        grid[y][x] = 'o'
# not 41513, 20757, 20756
