from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day20.py < sample.in
echo "=== real ===" ; py day20.py < day20.in
echo "=== sample ===" ; py day20.py < sample.in ; echo "=== real ===" ; py day20.py < day20.in
"""

# A = read_input('/dev/stdin')

f = open('/dev/stdin')
parts = f.read().strip().split('\n\n')

alg = ''.join(parts[0].strip().splitlines())

img = parts[1].strip().splitlines()


def automata(grid, iterations):
    flip = False
    for _ in range(iterations):
        if not flip:
            new_grid = defaultdict(lambda: '#')
        else:
            new_grid = defaultdict(lambda: '.')

        min_x = min(x for x, y in grid.keys())
        max_x = max(x for x, y in grid.keys())
        min_y = min(y for x, y in grid.keys())
        max_y = max(y for x, y in grid.keys())
        for i in range(min_x - 1, max_x + 2):
            for j in range(min_y - 1, max_y + 2):
                s = ''
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        s += grid[(i + ii, j + jj)]
                s = s.replace('#', '1')
                s = s.replace('.', '0')
                idx = int(s, 2)
                new_grid[i, j] = alg[idx]
        grid = new_grid
        flip = not flip
    return grid

res = 0
R = len(img)
C = len(img[0])
grid = defaultdict(lambda: '.')


for i in range(R):
    for j in range(C):
        grid[i, j] = img[i][j]


res = automata(grid, 50)
t = 0
for k, v in res.items():
    if v == '#':
        t += 1
print(t)
# != 5944
# != 7604
