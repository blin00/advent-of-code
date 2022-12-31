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
echo "=== sample ===" ; python3 day23.py < sample.in
echo "=== real ===" ; python3 day23.py < day23.in
echo "=== sample ===" ; python3 day23.py < sample.in ; echo "=== real ===" ; python3 day23.py < day23.in
"""

A = sys.stdin.read().rstrip('\n').splitlines()
N = len(A)

grid = set()

look_order = [
    (0, -1),    # north
    (0, 1),     # south
    (-1, 0),    # west
    (1, 0),     # east
]

adj = [
    [(0, -1), (1, -1), (-1, -1)],
    [(0, 1), (1, 1), (-1, 1)],
    [(-1, 0), (-1, -1), (-1, 1)],
    [(1, 0), (1, -1), (1, 1)],
]

for i, line in enumerate(A):
    for j, ch in enumerate(line):
        if ch == '#':
            grid.add((j, i))    # (x, y)

start_idx = 0

ROUNDS = 10

def print_grid(grid):
    min_x = min(x for x, y in grid)
    max_x = max(x for x, y in grid)
    min_y = min(y for x, y in grid)
    max_y = max(y for x, y in grid)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print('#' if (x, y) in grid else '.', end='')
        print()
    print()


ri = 0
while True:
    ri += 1
    ctr = Counter()
    proposal = []
    for x, y in grid:
        something_adj = False
        for nx, ny in n8(x, y):
            if (nx, ny) in grid:
                something_adj = True
                break
        if not something_adj:
            continue
        for i in range(4):
            idx = (start_idx + i) % 4
            something_adj = False
            for dx, dy in adj[idx]:
                nx, ny = x + dx, y + dy
                if (nx, ny) in grid:
                    something_adj = True
                    break
            if not something_adj:
                dx, dy = look_order[idx]
                proposal.append((x, y, x + dx, y + dy))
                ctr[(x + dx, y + dy)] += 1
                break
    moved = False
    for x, y, nx, ny in proposal:
        if ctr[(nx, ny)] == 1:
            moved = True
            grid.remove((x, y))
            grid.add((nx, ny))
    if not moved:
        print(ri)
        exit(0)
    start_idx = (start_idx + 1) % 4



min_x = min(x for x, y in grid)
max_x = max(x for x, y in grid)
min_y = min(y for x, y in grid)
max_y = max(y for x, y in grid)

res = 0
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if (x, y) not in grid:
            res += 1
print(res)