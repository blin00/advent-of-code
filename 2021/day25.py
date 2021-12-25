from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day25.py < sample.in
echo "=== real ===" ; py day25.py < day25.in
echo "=== sample ===" ; py day25.py < sample.in ; echo "=== real ===" ; py day25.py < day25.in
"""

A = read_input('/dev/stdin', t=list, strip_lines=True)

N = len(A)

res = 0

R = N
C = len(A[0])

it = 0
while True:
    moved = False
    
    delete = set()
    new = {}
    for i in range(R):
        for j in range(C):
            t = A[i][j]
            if t == '>':
                ii, jj = i, j + 1
                if jj >= C:
                    jj = 0
                if A[ii][jj] == '.':
                    moved = True
                    delete.add((i, j))
                    new[ii, jj] = '>'
    for i, j in delete:
        A[i][j] = '.'
    for (ii, jj), t in new.items():
        A[ii][jj] = t
    
    delete = set()
    new = {}
    for i in range(R):
        for j in range(C):
            t = A[i][j]
            if t == 'v':
                ii, jj = i + 1, j
                if ii >= R:
                    ii = 0
                if A[ii][jj] == '.':
                    moved = True
                    delete.add((i, j))
                    new[ii, jj] = 'v'
    for i, j in delete:
        A[i][j] = '.'
    for (ii, jj), t in new.items():
        A[ii][jj] = t

    it += 1
    if not moved:
        break

print(it)
