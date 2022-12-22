from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from math import gcd, lcm
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; pypy3 day18.py < sample.in
echo "=== real ===" ; pypy3 day18.py < day18.in
echo "=== sample ===" ; python3 day18.py < sample.in ; echo "=== real ===" ; python3 day18.py < day18.in
"""

A = sys.stdin.read().strip().splitlines()
N = len(A)


grid = set()

for line in A:
    x, y, z = ints(line, 3)
    grid.add((x, y, z))
res = 0

possible = Counter()

for pt in grid:
    for x, y, z in n4d(pt):
        if (x, y, z) not in grid:
            possible[(x, y, z)] += 1
            res += 1

dp = {}
def dfs(x, y, z, prv):
    stack = [(x, y, z, prv)]
    seen = set()
    while stack:
        x, y, z, prv = stack.pop()
        if (x, y, z) in dp:
            return dp[x, y, z]
        if abs(x) >= 25 or abs(y) >= 25 or abs(z) >= 25:
            dp[x, y, z] = True
            return True
        seen.add((x, y, z))
        for xx, yy, zz in n4d((x, y, z)):
            if (xx, yy, zz) in grid:
                continue
            if (xx, yy, zz) == prv:
                continue
            if (xx, yy, zz) in seen:
                continue
            stack.append((xx, yy, zz, (x, y, z)))
    dp[x, y, z] = False
    return False


for x, y, z in possible.keys():
    b = dfs(x, y, z, None)
    if not b:
        res -= possible[(x, y, z)]

print(res)