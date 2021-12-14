from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day14.py < sample.in
echo "=== real ===" ; py day14.py < day14.in
echo "=== sample ===" ; py day14.py < sample.in ; echo "=== real ===" ; py day14.py < day14.in
"""

f = open('/dev/stdin')
parts = f.read().strip().split('\n\n')

A = parts[0].strip()
B = parts[1].strip().splitlines()

dct = {}

for line in B:
    u, v = line.split(' -> ')
    dct[u] = v

def apply(s):
    N = len(s)
    insert_at = []
    for i in range(N - 1):
        a, b = s[i], s[i + 1]
        if a + b in dct:
            c = dct[a + b]
            insert_at.append(((i + 1), c))
        else:
            assert False
    assert insert_at
    i = 0
    j = 0
    res = []
    while True:
        if i == len(s):
            break
        if j == len(insert_at):
            res.append(s[i])
            i += 1
            continue
        if i == insert_at[j][0]:
            res.append(insert_at[j][1])
            j += 1
        else:
            res.append(s[i])
            i += 1
    return ''.join(res)

ctr = Counter()

for i in range(len(A) - 1):
    a, b = A[i], A[i + 1]
    d = a + b
    ctr[d] += 1

for it in range(40):
    nc = Counter()
    for k, v in ctr.items():
        middle = dct[k]
        a, b = k[0], k[1]
        nc[a + middle] += v
        nc[middle + b] += v
    ctr = nc

ctr2 = Counter()

for k, v in ctr.items():
    ctr2[k[0]] += v
    ctr2[k[1]] += v
ctr2[A[0]] += 1
ctr2[A[-1]] += 1

L = list(ctr2.items())
L.sort(key=lambda x: x[1])
print((L[-1][1] - L[0][1]) // 2)
