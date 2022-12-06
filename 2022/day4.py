from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day4.py < sample.in
echo "=== real ===" ; py day4.py < day4.in
echo "=== sample ===" ; py day4.py < sample.in ; echo "=== real ===" ; py day4.py < day4.in
"""

A = sys.stdin.read().strip().splitlines()

res = 0
res2 = 0

for line in A:
    p1, p2 = line.split(',')
    p1l, p1r = map(int, p1.split('-'))
    p2l, p2r = map(int, p2.split('-'))
    # check if one contains the other
    if p1l <= p2l <= p2r <= p1r:
        res += 1
    elif p2l <= p1l <= p1r <= p2r:
        res += 1

    # check if one overlaps
    if p1l <= p2l <= p1r or p2l <= p1l <= p2r:
        res2 += 1

print(res)
print(res2)
