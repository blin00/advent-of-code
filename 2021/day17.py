from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

XMIN = 79
XMAX = 137
YMIN = -176
YMAX = -117

# XMIN = 20
# XMAX = 30
# YMIN = -10
# YMAX = -5

res = 0

def simulate(vx, vy):
    x, y = 0, 0
    peak_y = 0
    good = False
    while True:
        x += vx
        y += vy
        peak_y = max(peak_y, y)
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        if XMIN <= x <= XMAX and YMIN <= y <= YMAX:
            good = True
            break
        if x > XMAX:
            good = False
            break
        if y < YMIN:
            good = False
            break
    return good, peak_y

res = 0

s = set()
for vx in range(1, 1000):
    for vy in range(-1000, 1000):
        g, r = simulate(vx, vy)
        if g:
            res = max(res, r)
            s.add((vx, vy))

print(res)
print(len(s))
