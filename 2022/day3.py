from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day3.py < sample.in
echo "=== real ===" ; py day3.py < day3.in
echo "=== sample ===" ; py day3.py < sample.in ; echo "=== real ===" ; py day3.py < day3.in
"""

A = sys.stdin.read().strip().splitlines()

def get_prio(c):
    if c in ascii_lowercase:
        return ascii_lowercase.index(c) + 1
    else:
        return ascii_uppercase.index(c) + 1 + 26

res = 0
for i in range(0, len(A), 3):
    a, b, c = A[i], A[i + 1], A[i + 2]
    d = set(ascii_lowercase) | set(ascii_uppercase)
    for line in (a, b, c):
        # l, r = line[:len(line)//2], line[len(line)//2:]
        d = d & set(line)
        # d = d & set(l)
        # d = d & set(r)
    for x in d:
        res += get_prio(x)



print(res)
