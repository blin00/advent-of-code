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

A = sys.stdin.read().strip()

_, moves = A.split('\n\n')

moves = moves.strip().splitlines()

"""
[V]     [B]                     [F]
[N] [Q] [W]                 [R] [B]
[F] [D] [S]     [B]         [L] [P]
[S] [J] [C]     [F] [C]     [D] [G]
[M] [M] [H] [L] [P] [N]     [P] [V]
[P] [L] [D] [C] [T] [Q] [R] [S] [J]
[H] [R] [Q] [S] [V] [R] [V] [Z] [S]
[J] [S] [N] [R] [M] [T] [G] [C] [D]
 1   2   3   4   5   6   7   8   9 
"""

state = [
    'VNFSMPHJ',
    'QDJMLRS',
    'BWSCHDQN',
    'LCSR',
    'BFPTVM',
    'CNQRT',
    'RVG',
    'RLDPSZC',
    'FBPGVJSD',
]

state = [list(x)[::-1] for x in state]

for line in moves:
    _, n, _, f, _, t = line.split()
    n = int(n)
    f = int(f)
    t = int(t)

    f -= 1
    t -= 1
    popped = []
    for i in range(n):
        x = state[f].pop()
        popped.append(x)
    popped = popped[::-1]
    state[t] += popped
    
res = []
for row in state:
    res.append(row[-1])
print(''.join(res))
