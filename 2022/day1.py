from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== real ===" ; py day1.py < day1.in
"""

A = sys.stdin.read().strip().split('\n\n')

b = []
res = 0
for group in A:
    val = sum(map(int, group.splitlines()))
    b.append(val)

b.sort()
b = b[::-1]
print(b[0])
print(sum(b[:3]))
