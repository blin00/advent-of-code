from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day8.py < sample.in
echo "=== real ===" ; py day8.py < day8.in
echo "=== sample ===" ; py day8.py < sample.in ; echo "=== real ===" ; py day8.py < day8.in
"""

A = sys.stdin.read().strip().splitlines()

res = 0

R = len(A)
C = len(A[0])

def visible(x, y):
    if x == 0 or x == R - 1 or y == 0 or y == C - 1:
        return True
    val = int(A[x][y])
    # to the up
    up = max([int(A[i][y]) for i in range(x)])
    if up < val:
        return True
    down = max([int(A[i][y]) for i in range(x + 1, R)])
    if down < val:
        return True
    left = max([int(A[x][i]) for i in range(y)])
    if left < val:
        return True
    right = max([int(A[x][i]) for i in range(y + 1, C)])
    if right < val:
        return True
    return False

def dist(x, y):
    up = [int(A[i][y]) for i in range(x - 1, -1, -1)]
    down = [int(A[i][y]) for i in range(x + 1, R)]
    left = [int(A[x][i]) for i in range(y - 1, -1, -1)]
    right = [int(A[x][i]) for i in range(y + 1, C)]
    val = int(A[x][y])
    def helper(arr):
        if not arr:
            return 0
        for i in range(len(arr)):
            if arr[i] >= val:
                return i + 1
        return len(arr)
    return helper(up) * helper(down) * helper(left) * helper(right)

res2 = 0
for i in range(R):
    for j in range(C):
        if visible(i, j):
            res += 1
        res2 = max(res2, dist(i, j))

print(res)
print(res2)
