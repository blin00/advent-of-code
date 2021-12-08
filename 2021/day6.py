from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day6.py < sample.in
echo "=== real ===" ; py day6.py < day6.in
echo "=== sample ===" ; py day6.py < sample.in ; echo "=== real ===" ; py day6.py < day6.in
"""
A = read_input('/dev/stdin')

A = map(int, A.split(','))
N = len(A)

DAYS = 256

ctr = [0] * 9

for x in A:
    ctr[x] += 1


for d in range(DAYS):
    new_ctr = [0] * 9
    for i, e in enumerate(ctr):
        if i == 0:
            new_ctr[8] += e
            new_ctr[6] += e
        else:
            new_ctr[i - 1] += e
    ctr = new_ctr

print(sum(ctr))