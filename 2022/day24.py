try:
    from sortedcontainers import *
    from math import gcd, lcm
except ImportError:
    pass
from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; pypy3 day24.py < sample.in
echo "=== real ===" ; pypy3 day24.py < day24.in
echo "=== sample ===" ; pypy3 day24.py < sample.in ; echo "=== real ===" ; pypy3 day24.py < day24.in
"""

A = sys.stdin.read().rstrip('\n').splitlines()
N = len(A)

res = 0
H = len(A)
W = len(A[0])

period = lcm(H - 2, W - 2)

grid = A

blizzards = []

for i in range(H):
    for j in range(W):
        if grid[i][j] == '>':
            blizzards.append((j, i, 1, 0))
        elif grid[i][j] == '<':
            blizzards.append((j, i, -1, 0))
        elif grid[i][j] == '^':
            blizzards.append((j, i, 0, -1))
        elif grid[i][j] == 'v':
            blizzards.append((j, i, 0, 1))

src = (grid[0].index('.'), 0)
tgt = (grid[-1].index('.'), H - 1)

assert grid[src[1]][src[0]] == '.'
assert grid[tgt[1]][tgt[0]] == '.'


def get_loc_after_time2(b, t):
    x, y, dx, dy = b
    x -= 1
    y -= 1

    x += dx * t
    y += dy * t
    x %= W - 2
    y %= H - 2

    x += 1
    y += 1
    return (x, y)


Q = deque()
Q.append((src, 574))     # partials: 0, 297, 574
seen = set()

last_t = -1

while Q:
    me, time = Q.popleft()
    nt = time + 1
    bad_set = set()
    if nt != last_t:
        last_t = nt
    for b in blizzards:
        bad_set.add(get_loc_after_time2(b, nt))
    for x, y in n5(*me, W, H):
        if (x, y) in bad_set:
            continue
        if grid[y][x] == '#':
            continue
        if (x, y) == tgt:
            print(nt)
            exit()
        ntp = nt % period
        if ((x, y), ntp) not in seen:
            seen.add(((x, y), ntp))
            Q.append(((x, y), nt))
