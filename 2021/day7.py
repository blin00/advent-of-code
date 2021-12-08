from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day7.py < sample.in
echo "=== real ===" ; py day7.py < day7.in
echo "=== sample ===" ; py day7.py < sample.in ; echo "=== real ===" ; py day7.py < day7.in
"""
A = read_input('/dev/stdin')

A = map(int, A.split(','))
N = len(A)

A.sort()

res = int(2e9)


for i in range(min(A), max(A) + 1):
    acc = 0
    for x in A:
        dist = abs(x - i)
        # acc += dist
        acc += dist * (dist + 1) // 2
    res = min(res, acc)

print(res)