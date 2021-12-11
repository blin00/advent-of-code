from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day11.py < sample.in
echo "=== real ===" ; py day11.py < day11.in
echo "=== sample ===" ; py day11.py < sample.in ; echo "=== real ===" ; py day11.py < day11.in
"""
A = read_input('/dev/stdin', t=lambda line: map(int, list(line)))
N = len(A)

res = 0
R = N
C = len(A[0])

def get_neighbors(i, j):
    # for ii, jj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
    for ii, jj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)):
        if 0 <= ii < R and 0 <= jj < C:
            yield ii, jj


def step(grid):
    new_grid = copy.deepcopy(grid)
    flashed = set()
    for i in range(R):
        for j in range(C):
            new_grid[i][j] += 1
    changed = True
    while changed:
        changed = False
        for i in range(R):
            for j in range(C):
                if new_grid[i][j] > 9 and (i, j) not in flashed:
                    flashed.add((i, j))
                    for ii, jj in get_neighbors(i, j):
                        new_grid[ii][jj] += 1
                        changed = True
    for i, j in flashed:
        new_grid[i][j] = 0
    return new_grid, len(flashed)

res = 0
grid = copy.deepcopy(A)
for i in range(100):
    grid, flashed = step(grid)
    res += flashed
print(res)

res = 0
grid = copy.deepcopy(A)
while True:
    res += 1
    grid, flashed = step(grid)
    if flashed == R * C:
        print(res)
        break
