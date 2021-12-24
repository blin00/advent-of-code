from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day22.py < sample.in
echo "=== real ===" ; py day22.py < day22.in
echo "=== sample ===" ; py day22.py < sample.in ; echo "=== real ===" ; py day22.py < day22.in
"""

A = read_input('/dev/stdin')

def add_interval(ss, L, R):
    assert L <= R
    if L == R:
        return None
    idx = ss.bisect_left((L, R))
    while idx < len(ss):
        ival = ss[idx]
        if ival[0] > R:
            break
        R = max(R, ival[1])
        ss.pop(idx)
    if idx > 0:
        idx -= 1
        ival = ss[idx]
        if ival[1] >= L:
            L = min(L, ival[0])
            R = max(R, ival[1])
            ss.pop(idx)
    res = (L, R)
    ss.add(res)
    return res

def remove_interval(ss, L, R):
    assert L <= R
    if L == R:
        return
    added = add_interval(ss, L, R)
    r2 = added[1]
    ss.remove(added)
    if added[0] != L:
        ss.add((added[0], L))
    if R != r2:
        ss.add((R, r2))

res = 0

N = len(A)

d = defaultdict(int)

B = []

for line in A:
    a, b = line.split(' ')
    x, y, z = b.split(',')

    L = []
    for c in (x, y, z):
        lo, hi = map(int, c[2:].split('..'))
        # if lo < -50: lo = -50
        # if hi > 50: hi = 50
        L.append((lo, hi))
    if a == 'on':
        L.append(1)
    elif a == 'off':
        L.append(0)
    else:
        assert False
    B.append(L)


z_events = defaultdict(list)

for x, y, z, a in B:
    z_events[z[0]].append(0)
    z_events[z[1] + 1].append(1)



def get_cells_on_at_z(desired_z):
    events = defaultdict(list)
    for x, y, z, a in B:
        if z[0] <= desired_z <= z[1]:
            xlo, xhi = x[0], x[1]
            ylo, yhi = y[0], y[1]
            events[ylo].append(0)
            events[yhi + 1].append(1)
    active = 0
    last_y = -99999999999
    res = 0
    for evt in sorted(events.keys()):
        ree = SortedSet()
        for x, y, z, a in B:
            if y[0] <= evt <= y[1] and z[0] <= desired_z <= z[1]:
                if a:
                    add_interval(ree, x[0], x[1] + 1)
                else:
                    remove_interval(ree, x[0], x[1] + 1)
        nactive = sum(b - a for a, b in ree)
        res += (evt - last_y) * active
        active = nactive
        last_y = evt
    assert active == 0
    return res

res = 0
active = 0
last_z = -99999999999
for evt in sorted(z_events.keys()):
    grid = defaultdict(int)
    nactive = get_cells_on_at_z(evt)
    res += (evt - last_z) * active
    active = nactive
    last_z = evt
assert active == 0
print(res)

    



#     for x in range(L[0][0], L[0][1] + 1):
#         for y in range(L[1][0], L[1][1] + 1):
#             for z in range(L[2][0], L[2][1] + 1):
#                 if a == 'on':
#                     d[(x, y, z)] = 1
#                 elif a == 'off':
#                     d[(x, y, z)] = 0
#                 else:
#                     assert False

#         for k in range(-50, 51):
#             res += d[(i, j, k)]

# print(res)
