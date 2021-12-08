from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day5.py < sample.in
echo "=== real ===" ; py day5.py < day5.in
echo "=== sample ===" ; py day5.py < sample.in ; echo "=== real ===" ; py day5.py < day5.in
"""
A = read_input('/dev/stdin')
N = len(A)
R = N

lines = []

for line in A:
    a, b = line.split(' -> ')
    a1, a2 = map(int, a.split(','))
    b1, b2 = map(int, b.split(','))
    lines.append(((a1, a2), (b1, b2)))

count = defaultdict(int)

for line in lines:
    a, b = line
    if a[0] == b[0]:
        u, v = sorted((a[1], b[1]))
        for i in range(u, v + 1):
            count[(a[0], i)] += 1
    elif a[1] == b[1]:
        u, v = sorted((a[0], b[0]))
        for i in range(u, v + 1):
            count[(i, a[1])] += 1
    else:
        if a[0] > b[0]:
            a, b = b, a
        # diag up
        if a[1] < b[1]:
            for i in range(a[0], b[0] + 1):
                count[(i, a[1] + i - a[0])] += 1
        else:
            for i in range(a[0], b[0] + 1):
                count[(i, a[1] - i + a[0])] += 1
        # diag down

res = 0
for k, v in count.items():
    if v >= 2:
        res += 1
print(res)
