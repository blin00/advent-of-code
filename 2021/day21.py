from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day21.py < sample.in
echo "=== real ===" ; py day21.py < day21.in
echo "=== sample ===" ; py day21.py < sample.in ; echo "=== real ===" ; py day21.py < day21.in
"""

res = 0

START = [7, 5]
# START = [4, 8]
THRESHOLD = 1000

ree = 1
rc = 0
def roll():
    global ree, rc
    res = ree
    ree += 1
    if ree > 100:
        ree = 1
    rc += 1
    return res


p1, p2 = START
p1s, p2s = 0, 0
while True:
    s = sum([roll() for _ in range(3)])
    p1 += s
    while p1 > 10:
        p1 -= 10
    p1s += p1
    if p1s >= THRESHOLD:
        break
    s = sum([roll() for _ in range(3)])
    p2 += s
    while p2 > 10:
        p2 -= 10
    p2s += p2
    if p2s >= THRESHOLD:
        break

print(min(p1s, p2s) * rc)


p1win = 0
p2win = 0
THRESHOLD = 21
ctr = Counter()
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            d = i + j + k
            ctr[d] += 1

def go(p1turn, p1, p2, p1s, p2s, mult):
    global p1win, p2win

    for k, v in ctr.items():
        np1 = p1 + k
        while np1 > 10:
            np1 -= 10
        np1s = p1s + np1
        if np1s >= THRESHOLD:
            if p1turn:
                p1win += v * mult
            else:
                p2win += v * mult
            continue
        go(not p1turn, p2, np1, p2s, np1s, mult * v)

go(True, START[0], START[1], 0, 0, 1)

print(p1win, p2win, max(p1win, p2win))
