# from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; pypy3 day12.py < sample.in
echo "=== real ===" ; pypy3 day12.py < day12.in
echo "=== sample ===" ; pypy3 day12.py < sample.in ; echo "=== real ===" ; pypy3 day12.py < day12.in
"""

A = sys.stdin.read().strip().splitlines()
# A = sys.stdin.read().strip().split('\n\n')

N = len(A)
M = len(A[0])

for i in range(N):
    for j in range(M):
        if A[i][j] == 'S':
            end_i = i
            end_j = j
        elif A[i][j] == 'E':
            start_i = i
            start_j = j


Q = deque()
Q.append((start_i, start_j, 0))
visited = set()

def conv(c):
    if c == 'S':
        return 'a'
    elif c == 'E':
        return 'z'
    return c


res = 1e18
while Q:
    i, j, d = Q.popleft()
    if (i, j) in visited:
        continue
    visited.add((i, j))
    for ii, jj in n4(i, j, N, M):
        if ord(conv(A[i][j])) <= ord(conv(A[ii][jj])) + 1:
            Q.append((ii, jj, d + 1))
    if conv(A[i][j]) == 'a':
        res = min(res, d)
print(res)
