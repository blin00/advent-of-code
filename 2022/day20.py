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
echo "=== sample ===" ; pypy3 day20.py < sample.in
echo "=== real ===" ; pypy3 day20.py < day20.in
echo "=== sample ===" ; pypy3 day20.py < sample.in ; echo "=== real ===" ; pypy3 day20.py < day20.in
"""

A = sys.stdin.read().strip().splitlines()
N = len(A)

A = map(int, A)

KEY = 811589153
A = map(lambda x: x * KEY, A)

A = list(enumerate(A))

def mix(A):
    def f(idx):
        for i in range(len(A)):
            if A[i][0] == idx:
                return i
        assert False
    for i in range(len(A)):
        idx = f(i)
        val = A[idx][1]
        if val > 0:
            val %= (N - 1)
        elif val < 0:
            val = -((-val) % (N - 1))
        while val != 0:
            if val > 0:
                tgt = (idx + 1) % N
                A[tgt], A[idx] = A[idx], A[tgt]
                idx += 1
                idx %= N
                val -= 1
            else:
                tgt = (idx - 1) % N
                A[tgt], A[idx] = A[idx], A[tgt]
                idx -= 1
                idx %= N
                val += 1
    return A

for i in range(10):
    A = mix(A)

tgt = -1
for i in range(N):
    if A[i][1] == 0:
        tgt = i
        break
assert tgt >= 0

offsets = [1000, 2000, 3000]
res = []
for offset in offsets:
    idx = tgt + offset
    idx %= N
    res.append(A[idx][1])
print(res, sum(res))
# not -872458339475
# not -1470