from sortedcontainers import *

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
A = read_input('/dev/stdin')
N = len(A)

res = 0

R = N
C = len(A[0])

def get_neighbors(i, j):
    for ii, jj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
    # for ii, jj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)):
        if 0 <= ii < R and 0 <= jj < C:
            yield ii, jj

lpts = []

for i in range(R):
    for j in range(C):
        low = True
        for ii, jj in get_neighbors(i, j):
            if A[ii][jj] <= A[i][j]:
                low = False
                break
        if low:
            lpts.append((i, j))
            res += 1 + int(A[i][j])
print(res)

ls = set(lpts)

def flow(i, j, s):
    s.add((i, j))
    if (i, j) in ls:
        return (i, j)

    basin = None
    for ii, jj in get_neighbors(i, j):
        if A[ii][jj] < A[i][j]:
            basin = flow(ii, jj, s)
    return basin

r2 = defaultdict(set)

for i in range(R):
    for j in range(C):
        if A[i][j] == '9':
            continue
        s = set()
        basin = flow(i, j, s)
        r2[basin] |= s

L = sorted(r2.items(), key=lambda x: -len(x[1]))

print(prod(map(lambda x: len(x[1]), L[:3])))
