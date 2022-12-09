# from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day9.py < sample.in
echo "=== real ===" ; py day9.py < day9.in
echo "=== sample ===" ; py day9.py < sample.in ; echo "=== real ===" ; py day9.py < day9.in
"""

A = sys.stdin.read().strip().splitlines()

visited = set()

hx, hy = 0, 0
tx, ty = 0, 0

visited.add((tx, ty))

knots = [[0, 0] for _ in range(10)]

for line in A:
    d, c = line.split()
    d = DIRS_M[d]
    c = int(c)
    dxx, dyy = DIRS[d]
    for i in range(c):
        knots[0][0] += dxx
        knots[0][1] += dyy
        for ti in range(1, len(knots)):
            hx = knots[ti - 1][0]
            hy = knots[ti - 1][1]
            tx = knots[ti][0]
            ty = knots[ti][1]
            if hx == tx:
                if abs(hy - ty) >= 2:
                    if ty > hy:
                        ty -= 1
                    else:
                        ty += 1
            elif hy == ty:
                if abs(hx - tx) >= 2:
                    if tx > hx:
                        tx -= 1
                    else:
                        tx += 1
            else:
                if abs(hx - tx) >= 2 or abs(hy - ty) >= 2:
                    dx = sgn(hx - tx)
                    dy = sgn(hy - ty)
                    assert dx and dy
                    tx += dx
                    ty += dy
            knots[ti][0] = tx
            knots[ti][1] = ty
        visited.add((knots[-1][0], knots[-1][1]))
        

print(len(visited))

