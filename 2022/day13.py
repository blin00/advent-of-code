# from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; pypy3 day13.py < sample.in
echo "=== real ===" ; pypy3 day13.py < day13.in
echo "=== sample ===" ; pypy3 day13.py < sample.in ; echo "=== real ===" ; pypy3 day13.py < day13.in
"""

# A = sys.stdin.read().strip().splitlines()
A = sys.stdin.read().strip().split('\n\n')

N = len(A)

def cmp(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a < b
    elif isinstance(a, list) and isinstance(b, list):
        for i in range(len(a)):
            if i >= len(b):
                return False
            if cmp(a[i], b[i]):
                return True
            elif cmp(b[i], a[i]):
                return False
            else:
                pass
        if len(a) < len(b):
            return True
        return False
    else:
        if isinstance(a, int):
            a = [a]
        if isinstance(b, int):
            b = [b]
        return cmp(a, b)

def cmp2(a, b):
    if cmp(a, b):
        return -1
    elif cmp(b, a):
        return 1
    else:
        return 0

res = []
B = []
for i, pair in enumerate(A):
    p1, p2 = pair.splitlines()
    p1, p2 = map(eval, (p1, p2))
    B.append(p1)
    B.append(p2)
    if cmp(p1, p2):
        res.append(i + 1)
B.append([[2]])
B.append([[6]])
print(res, sum(res))

B.sort(key=cmp_to_key(cmp2))

l = -1
m = -1

for i, arr in enumerate(B):
    if arr == [[2]]:
        l = i + 1
    if arr == [[6]]:
        m = i + 1

print(l, m, l * m)